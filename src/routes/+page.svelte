<script lang="ts">
	import { source } from 'sveltekit-sse';
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

<h1>Playtest</h1>

<label for="grep">Filter<input bind:value={grep} id="grep" name="grep" type="text" /></label>
<button id="runBtn" onclick={openStream}>Run</button>

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
