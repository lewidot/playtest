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

<div class="flex-1 space-y-4 p-8 pt-6">
	<div class="flex items-center justify-between space-y-2">
		<h2 class="text-3xl font-bold tracking-tight">Test runner</h2>
		<GitInfo commit={data.commit} message={data.message} />
	</div>
	<div class="space-y-4">
		<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-8">
			<div class="col-span-6 h-[600px] overflow-auto rounded-md border p-4">
				{#each runOutput.values as message}
					<pre class="font-mono text-sm">{message}</pre>
				{/each}
			</div>
			<div class="col-span-2 h-full rounded-md border p-4">
				<div class="my-4 flex-col space-y-4 sm:flex md:order-2">
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
			</div>
		</div>
	</div>
</div>
