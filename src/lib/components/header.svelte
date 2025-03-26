<script lang="ts">
	import RunStatus from '$lib/components/run-status.svelte';
</script>

<header
	class="flex items-start justify-between space-y-2 p-10 sm:flex-row sm:items-center sm:space-y-0 md:h-16"
>
	<a href="/">
		<div class="flex items-center gap-2">
			<img src="/theater.png" class="size-8" alt="logo" />
			<h1 class="text-3xl font-bold">Playtest</h1>
		</div></a
	>
	<RunStatus />
</header>
