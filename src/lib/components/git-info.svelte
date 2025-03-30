<script lang="ts">
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import LoaderCircle from 'lucide-svelte/icons/loader-circle';
	import * as Dialog from '$lib/components/ui/dialog';

	let { commit, message }: { commit: string; message: string } = $props();
	let disabled = $state(false);

	// Function to fetch the latest commit for the tmp/ repository.
	async function fetchLatestCommit() {
		disabled = true;
		const res = await fetch('/commit', {
			method: 'GET'
		});

		const data = await res.json();
		commit = data.commit;
		message = data.message;

		disabled = false;
	}
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline' })}>Project Info</Dialog.Trigger>
	<Dialog.Content class="sm:max-w-[425px]">
		<Dialog.Header>
			<Dialog.Title>Project Information</Dialog.Title>
			<Dialog.Description>Git data for the Playwright project.</Dialog.Description>
		</Dialog.Header>
		<section class="pb-8">
			<ul class="space-y-1">
				<li class="text-sm font-semibold">
					commit: <span class="font-mono text-xs font-normal">{commit}</span>
				</li>
				<li class="text-sm font-semibold">
					commit message: <span class="font-mono text-xs font-normal">{message}</span>
				</li>
			</ul>
		</section>

		<Dialog.Footer>
			<Button {disabled} type="submit" onclick={fetchLatestCommit}
				>{#if disabled}
					<LoaderCircle class="animate-spin" />
					Fetching latest commit
				{:else}
					Fetch latest commit
				{/if}</Button
			>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
