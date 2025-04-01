import { produce } from 'sveltekit-sse';
import type { RequestHandler } from './$types';
import { playwrightEmitter } from '$lib';

export const POST: RequestHandler = async () => {
	// Return the produce function from 'sveltekit-sse' that handles streaming the response.
	return produce(async function start({ emit }) {
		// Create a function so we can remove it when the client disconnects
		const send = (msg: string) => {
			const { error } = emit('message', msg);
			// We errored sending to client - likely because they've disconnected
			if (error) {
				return cancel();
			}
		};

		const cancel = () => {
			// Avoid memory leaks by removing the listener when the client is gone
			playwrightEmitter.removeListener('stdout', send);
		};

		playwrightEmitter.on('stdout', send);
		// Return a reference to the cancel function so clean up can happen when the library detects that the client has disconnected
		return cancel;
	});
};
