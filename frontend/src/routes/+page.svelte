<script>
	import { onMount } from 'svelte';
	import Todo from '$lib/todo/todo.svelte';
	import { todos, url } from '../store.js';
	import Add from '$lib/add.svelte';

	onMount(() => {
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				todos.set(data);
			});
	});
</script>

<main>
	<Add />
	<div
		class="h-[calc(calc(100*var(--vh))-10rem)] grid place-items-center gap-5 overflow-scroll m-5"
	>
		{#each $todos as task}
			<Todo {task} />
		{/each}
	</div>
</main>
