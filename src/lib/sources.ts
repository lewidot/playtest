import { source } from 'sveltekit-sse';

export const runSource = source('/api/run');
export const statusSource = source('/api/status');

// create watcher to avoid the store becoming inactive 'https://github.com/razshare/sveltekit-sse/issues/61'
runSource.select('message').subscribe(function watcher(value) {
	console.log(value);
});

statusSource.select('message').subscribe(function watcher(value) {
	console.log(value);
});
