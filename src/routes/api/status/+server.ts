import { produce } from 'sveltekit-sse';
import { storeEmitter } from '$lib';

export function POST() {
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
			storeEmitter.removeListener('running', send);
		};

		storeEmitter.on('running', send);
		// Return a reference to the cancel function so clean up can happen when the library detects that the client has disconnected
		return cancel;
	});
}
