<script lang="ts">
	import RunStatus from '$lib/components/run-status.svelte';
	import MainNav from '$lib/components/main-nav.svelte';
</script>

<header class="flex-col md:flex">
	<div class="border-b">
		<div class="flex h-16 items-center px-4">
			<a href="/">
				<div class="flex items-center gap-2">
					<img src="/theater.png" class="size-8" alt="logo" />
					<h1 class="text-3xl font-bold">Playtest</h1>
				</div></a
			>
			<MainNav />
			<div class="ml-auto flex items-center space-x-4">
				<RunStatus />
			</div>
		</div>
	</div>
</header>
