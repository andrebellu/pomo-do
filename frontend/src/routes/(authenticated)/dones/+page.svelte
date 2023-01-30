<script>
	import { onMount } from 'svelte';
	import Todo from '$lib/todo/todo.svelte';
	import { todos, url, tomorrow } from '../../../store.js';
	import { fly, fade } from 'svelte/transition';

	onMount(() => {
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				todos.set(data);
			});
	});
</script>

<main in:fly={{ y: 200, duration: 1000, delay: 500 }} out:fade>
	<div class="flex items-center justify-center max-h-screen">
		<a
			class="text-white btn bg-info material-symbols-outlined rounded-full ml-3 hover:bg-blue-300 transition-all duration-300 ease-in-out"
			aria-hidden="true"
			href="/">undo</a
		>
	</div>
	<div class="h-[75vh] overflow-scroll m-5 items-top flex justify-center">
		<div class="max-h-full flex flex-col gap-5 overflow-auto m-5 scrollbar-hide">
			{#each $todos as task}
				{#if task.stato == true}
					<Todo {task} />
				{/if}
			{/each}
		</div>
	</div>
</main>
