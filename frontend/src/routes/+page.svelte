<script>
	import { onMount } from 'svelte';
	import Todo from '$lib/todo/todo.svelte';
	import { todos, url, tomorrow } from '../store.js';
	import Add from '$lib/add.svelte';
	import Filters from '../lib/filters.svelte';
	import Spinner from '../lib/spinner.svelte';

	onMount(() => {
		fetch(url)
			.then((response) => response.json())
			.then((data) => {
				todos.set(data);
			});
	});

	function isTomorrow(date) {
		if (
			new Date(date).getDate() == new Date().getDate() + 1 &&
			new Date(date).getMonth() == new Date().getMonth() &&
			new Date(date).getFullYear() == new Date().getFullYear()
		) {
			return true;
		}
	}
</script>

<main>
	<Add />
	<Filters />
	<div class="h-screen m-5 items-top flex justify-center">
		<div class="max-h-full flex flex-col gap-5 scrolling-auto overflow-auto m-5 scrollbar-hide">
			{#if $todos.length == 0}
				<div class="flex justify-center">
					<Spinner />
				</div>
			{:else if $tomorrow == true}
				{#each $todos as task}
					{#if isTomorrow(task.data) && task.stato == 0}
						<Todo {task} />
					{/if}
				{/each}
			{:else}
				{#each $todos as task}
					{#if task.stato == 0}
						<Todo {task} />
					{/if}
				{/each}
			{/if}
		</div>
	</div>
</main>
