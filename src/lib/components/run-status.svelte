<script lang="ts">
	import { statusSource } from '$lib/sources';
	import { runOutput, runState } from '$lib/state.svelte';

	let msg = $derived.by(() => {
		if (runState.value === true) {
			return 'playwright running';
		} else {
			return 'playwright not running';
		}
	});

	// Connect to /api/status stream to listen for changes to the state of the playwright run.
	// '0' for when playwright is not running
	// '1' for when a playwright test run is active
	const stream = statusSource.select('message');
	// Subscribe to messages
	stream.subscribe((message: string) => {
		// Update the global run state.
		if (message === '1') {
			runState.value = true;
			runOutput.values = [''];
		} else {
			runState.value = false;
		}
	});
</script>

<span
	class="inline-flex items-center justify-center rounded-full {runState.value
		? 'bg-emerald-100 text-emerald-700'
		: 'bg-red-100 text-red-700'} px-2.5 py-0.5"
>
	<p class="whitespace-nowrap text-sm">{msg}</p>
</span>
