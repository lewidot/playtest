import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { setStore } from '$lib';
import { spawn } from 'child_process';
import stripAnsi from 'strip-ansi';
import { playwrightEmitter } from '$lib';
import log from '$lib/logger';
import type { RunOptions } from '$lib/types';

export const POST: RequestHandler = async ({ request }) => {
	// Handle the POST request here
	const body = (await request.json()) as RunOptions;

	//Base arguments for the playwright cli.
	const args = ['exec', 'playwright', 'test'];

	// If a grep value is specified, add to playwright cli args.
	if (body.grep !== '') {
		args.push('-g', body.grep);
	}

	// Spawn the process that runs the playwright tests.
	const child = spawn('pnpm', args, {
		cwd: './tmp'
	});

	child.on('spawn', () => {
		log.info({ pid: child.pid }, 'child process started');
		const msg = `Run command: ${child.spawnargs.join(' ')}`;
		playwrightEmitter.emit('stdout', msg);
	});

	// Set run value in the store to 1.
	setStore(1);

	//As each data event is emitted, clean up the data and then emit a message.
	child.stdout.on('data', (data) => {
		const stringData = data.toString();
		const stripped = stripAnsi(stringData);
		playwrightEmitter.emit('stdout', stripped);
	});

	child.stderr.on('data', (data) => {
		const stringData = data.toString();
		const stripped = stripAnsi(stringData);
		playwrightEmitter.emit('stdout', stripped);
	});

	child.on('error', (error) => {
		log.info({ pid: child.pid, error: error.message }, `child process error`);
		const stripped = stripAnsi(error.message);
		playwrightEmitter.emit('stdout', stripped);
		playwrightEmitter.emit('stdout', 'error');
	});

	// When the process closes, handle any cleanup and emit a final message to the client to signal it has completed.
	child.on('close', (code) => {
		log.info({ pid: child.pid }, `child process exited with code ${code}`);
		setStore(0);
		playwrightEmitter.emit('stdout', 'end');
	});

	return json({ message: 'ok' });
};
