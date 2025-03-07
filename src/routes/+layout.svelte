<script lang="ts">
	import { Toaster } from '$lib/components/ui/sonner/index.js';
	import '../app.css';
	let { children } = $props();
</script>

<Toaster richColors />

<div class="container">
	<div
		class="flex flex-col items-start justify-between space-y-2 p-10 sm:flex-row sm:items-center sm:space-y-0 md:h-16"
	>
		<a href="/">
			<div class="flex items-center gap-2">
				<img src="/theater.png" class="size-8" alt="logo" />
				<h1 class="text-3xl font-bold">Playtest</h1>
			</div></a
		>
	</div>

	<main class="container h-[calc(100vh-80px)] py-6">{@render children()}</main>
</div>
