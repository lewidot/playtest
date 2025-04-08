<script lang="ts">
	import { Toaster } from '$lib/components/ui/sonner/index.js';
	import '../app.css';
	import Header from '$lib/components/header.svelte';
	import { runSource } from '$lib/sources';
	import { toast } from 'svelte-sonner';
	import { runOutput } from '$lib/state.svelte';

	let { children } = $props();

	// Connect to /api/run stream to listen for the output of the playwright run.
	// 'end' for when the playwright run is complete
	const runStream = runSource.select('message');
	// Subscribe to messages
	runStream.subscribe((message: string) => {
		// Close the connection when the "end" message has been received.
		if (message === 'end') {
			// Show toast
			toast.success('Test run complete');
			return;
		} else if (message === 'error') {
			// Show toast
			toast.error('Error running tests');
			return;
		}

		// Update the array of messages.
		runOutput.values.push(message);
	});
</script>

<Toaster richColors />

<div class="container pt-5">
	<Header />

	<main class="container h-[calc(100vh-100px)] pb-6">{@render children()}</main>
</div>
