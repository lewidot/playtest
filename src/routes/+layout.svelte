<script lang="ts">
	import { Toaster } from '$lib/components/ui/sonner/index.js';
	import '../app.css';
	import Header from '$lib/components/header.svelte';

	let { children } = $props();
</script>

<Toaster richColors />

<div class="container">
	<Header />

	<main class="container h-[calc(100vh-80px)] pb-6">{@render children()}</main>
</div>
