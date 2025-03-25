import { EventEmitter } from 'events';

// Event Emitter for sending playwright output to the '/run' SSE endpoint.
export const playwrightEmitter: EventEmitter = new EventEmitter();

// Event Emitter for notifying changes to the store.
export const storeEmitter: EventEmitter = new EventEmitter();

// Map to set whether Playwright is running or not.
export const store = new Map<string, number>([['running', 0]]);

// Set the value for 'running' and emit the event.
export function setStore(value: number) {
	store.set('running', value);
	storeEmitter.emit('running', value.toString());
}
