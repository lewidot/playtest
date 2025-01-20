<script lang="ts">
	import { source } from 'sveltekit-sse';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';

	let messages = $state(['']);
	let grep = $state('');

	function openStream() {
		messages = [''];
		let btn = document.getElementById('runBtn') as HTMLButtonElement;
		btn.disabled = true;
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
				btn.disabled = false;
				return;
			}

			// Update the array of messages.
			messages.push(message);
		});
	}
</script>

<h1 class="text-4xl font-semibold">Playtest</h1>

<div class="w-2/3 space-y-6">
	<div class="flex w-full max-w-sm flex-col gap-1.5">
		<Label for="grep">Filter</Label>
		<Input type="text" id="grep" name="grep" bind:value={grep} />
	</div>

	<Button id="runBtn" onclick={openStream}>Run</Button>
</div>

<!-- Display messages -->
<div class="message-container">
	{#each messages as message}
		<pre>{message}</pre>
	{/each}
</div>

<style>
	.message-container {
		border-width: 1px;
		border-color: black;
		border-style: solid;
		border-radius: 6px;
		min-height: 60px;
		padding: 1em;
		margin-top: 2em;
		min-width: 50%;
		max-width: 75%;
	}
</style>
