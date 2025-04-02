<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import LoaderCircle from 'lucide-svelte/icons/loader-circle';
	import { runState, runOutput } from '$lib/state.svelte';
	import type { PageProps } from './$types';
	import GitInfo from '$lib/components/git-info.svelte';
	import { toast } from 'svelte-sonner';

	// Server loaded page data
	let { data }: PageProps = $props();

	// Set reactive state
	let grep = $state('');
	let disabled = $derived(runState.value);

	// Function to post data to the /start endpoint and start the playwright run.
	async function start() {
		await fetch('/api/start', {
			method: 'POST',
			body: JSON.stringify({ grep: grep })
		});
		toast.info('Test run started', {});
	}
</script>

<GitInfo commit={data.commit} message={data.message} />
<div class="grid h-full items-stretch gap-6 md:grid-cols-[1fr_300px]">
	<div class="my-4 hidden flex-col space-y-4 sm:flex md:order-2">
		<div class="mb-4 grid gap-2">
			<Label for="grep">Filter</Label>
			<Input type="text" id="grep" name="grep" bind:value={grep} />
		</div>
		<Button {disabled} id="runBtn" onclick={start}
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
			<div
				class="my-4 max-h-[700px] min-h-[400px] w-full flex-1 overflow-auto rounded-md border p-4 shadow-sm md:text-sm"
			>
				{#each runOutput.values as message}
					<pre class="font-mono text-sm">{message}</pre>
				{/each}
			</div>
		</div>
	</div>
</div>
