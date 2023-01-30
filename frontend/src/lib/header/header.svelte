<script>
	import Hamburger from '$lib/menu/hamburger.svelte';
	import Menu from '$lib/menu/menu.svelte';

	export let open = false;
	export let onClick = () => {
		open = !open;
	};
</script>

<main>
	<div class="navbar bg-invisible md:hidden mb-5">
		<Hamburger {open} {onClick} />
		<h1 class="text-4xl text-primary">Pomodò</h1>
	</div>

	<div
		class="navbar bg-invisible hidden m-0 w-0 p-0 md:visible md:w-full md:flex md:justify-between md:mb-5"
	>
		<h1 class="text-4xl text-primary mx-10">Pomodò</h1>
		<div class="flex gap-10 mx-10">
			<a class="text-2xl text-primary element" href="/">Todos</a>
			<a class="text-2xl text-primary element" href="/pomodoro">Pomodoro</a>
			<a class="text-2xl text-primary element" href="/statistics">Statistics</a>
		</div>
	</div>

	{#if open}
		<div class="page h-screen w-screen flex justify-center items-center bg-base-100 absolute z-50">
			<Menu />
		</div>
	{/if}
</main>
