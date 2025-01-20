<script lang="ts">
	import { source } from 'sveltekit-sse';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import LoaderCircle from 'lucide-svelte/icons/loader-circle';
	import { toast } from 'svelte-sonner';

	let messages = $state(['']);
	let grep = $state('');
	let disabled = $state(false);

	function openStream() {
		messages = [''];
		disabled = true;

		// POST to "/run" and listen for "message" events
		const connection = source('/run', {
			cache: false,
			open() {
				console.log('opening connection to /run');
			},
			close() {
				console.log('closing connection to /run');
			},
			options: {
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ grep: grep })
			}
		});

		const stream = connection.select('message');

		// Subscribe to messages
		stream.subscribe((message: string) => {
			// Close the connection when the "end" message has been received.
			if (message === 'end') {
				connection.close();

				// Enable the Run button
				disabled = false;

				// Show toast
				toast.success('Test run complete');
				return;
			}

			// Update the array of messages.
			messages.push(message);
		});
	}
</script>

<div class="w-2/3 space-y-6">
	<div class="flex w-full max-w-sm flex-col gap-1.5">
		<Label for="grep">Filter</Label>
		<Input type="text" id="grep" name="grep" bind:value={grep} />
	</div>

	<Button {disabled} id="runBtn" onclick={openStream}
		>{#if disabled}
			<LoaderCircle class="animate-spin" />
			Running
		{:else}
			Run
		{/if}</Button
	>
</div>

<!-- Display messages -->
<div class="my-4 min-h-16 overflow-auto rounded-sm border border-slate-900 p-4">
	{#each messages as message}
		<pre class="p-1">{message}</pre>
	{/each}
</div>
