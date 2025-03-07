<script lang="ts">
	import { source } from 'sveltekit-sse';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import LoaderCircle from 'lucide-svelte/icons/loader-circle';
	import { toast } from 'svelte-sonner';
	import { type RunOptions } from '$lib/types';

	let messages = $state(['']);
	let grep = $state('');
	let disabled = $state(false);

	function openStream() {
		messages = [''];
		disabled = true;
		const runBody: RunOptions = { grep: grep };

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
				body: JSON.stringify(runBody)
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

<div class="grid h-full items-stretch gap-6 md:grid-cols-[1fr_200px]">
	<div class="my-4 hidden flex-col space-y-4 sm:flex md:order-2">
		<div class="mb-4 grid gap-2">
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
	<div class="md:order-1">
		<div class="flex h-full flex-col space-y-4">
			<!-- Display messages -->
			<div
				class="my-4 max-h-[700px] min-h-[400px] w-full flex-1 overflow-auto rounded-md border p-4 shadow-sm md:text-sm"
			>
				{#each messages as message}
					<pre class="font-mono text-sm">{message}</pre>
				{/each}
			</div>
		</div>
	</div>
</div>
