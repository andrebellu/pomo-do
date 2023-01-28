<script>
	import { onMount } from 'svelte';
	import Todo from '$lib/todo/todo.svelte';
	import { todos, url, tomorrow } from '../store.js';
	import Add from '$lib/add.svelte';
	import Filters from '../lib/filters.svelte';

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
	<Filters />
	<div class="h-screen m-5 items-top flex justify-center">
		<div class="max-h-full flex flex-col gap-5 scrolling-auto overflow-auto m-5 scrollbar-hide">
			{#if $tomorrow == true}
				{#each $todos as task}
					{#if new Date(task.data).getDate() == new Date().getDate() + 1}
						<Todo {task} />
					{/if}
				{/each}
			{:else}
				{#each $todos as task}
					<Todo {task} />
				{/each}
			{/if}
		</div>
	</div>
</main>
