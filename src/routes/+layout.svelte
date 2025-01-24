<script lang="ts">
	import { Toaster } from '$lib/components/ui/sonner/index.js';
	import '../app.css';
	let { children } = $props();
</script>

<Toaster richColors />
<header class="mx-auto flex max-w-screen-md items-center justify-center px-12 py-4">
	<a href="/">
		<div class="flex items-center gap-2">
			<img src="/theater.png" class="size-8" alt="logo" />
			<h1 class="text-3xl font-bold">Playtest</h1>
		</div></a
	>
</header>

<div class="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8">
	<div class="mx-auto max-w-2xl">
		{@render children()}
	</div>
</div>
