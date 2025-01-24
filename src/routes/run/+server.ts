import { produce } from 'sveltekit-sse';
import { spawn } from 'child_process';
import stripAnsi from 'strip-ansi';
import type { RequestHandler } from './$types';
import type { RunOptions } from '$lib/types';

export const POST: RequestHandler = async ({ request }) => {
	// Handle the POST request here
	const body = (await request.json()) as RunOptions;

	// Return the produce function from 'sveltekit-sse' that handles streaming the response.
	return produce(async function start({ emit }) {
		// Base arguments for the playwright cli.
		const args = ['exec', 'playwright', 'test'];

		// If a grep value is specified, add to playwright cli args.
		if (body.grep !== '') {
			args.push('-g', body.grep);
		}
		// Spawn the process that runs the playwright tests.
		const child = spawn('pnpm', args, {
			cwd: './tmp'
		});

		// As each data event is emitted, clean up the data and then stream a message.
		child.stdout.on('data', (data) => {
			const stringData = data.toString();
			const stripped = stripAnsi(stringData);
			const { error } = emit('message', stripped);
			if (error) {
				console.error('error whilst streaming');
				return;
			}
		});

		child.stderr.on('data', (data) => {
			console.error(`stderr: ${data}`);
		});

		child.on('error', (err) => {
			console.error(`stderr: ${err}`);
		});

		// When the process closes, handle any cleanup and send a final message to the client to signal it has completed.
		child.on('close', (code) => {
			console.log(`child process exited with code ${code}`);
			const { error } = emit('message', 'end');
			if (error) {
				console.log('error whilst streaming');
				return;
			}
		});
	});
};
