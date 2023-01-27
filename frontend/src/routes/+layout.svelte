<script>
	import '../app.css';
	import Header from '$lib/header/header.svelte';

	import { page } from '$app/stores';
</script>

<main>
	{#if $page.path !== '/login'}
		<Header />
	{/if}
	<slot />
</main>
