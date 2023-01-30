<script>
	export let task;
	import { todos, url } from '../../store.js';

	async function doneTodo(id) {
		const options = {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json'
			}
		};

		const response = await fetch(url + '/' + id, options);
		const data = await response.json();
		await refresh();
	}

	async function refresh() {
		const response = await fetch(url);
		const data = await response.json();
		todos.set(data);
	}
</script>

<main>
	{#if !task.stato}
		<button
			class="btn btn-primary btn-circle material-symbols-outlined text-xl"
			on:click={() => doneTodo(task.id)}>done</button
		>
	{:else}
		<button
			class="btn btn-primary btn-circle material-symbols-outlined text-xl"
			on:click={() => doneTodo(task.id)}>redo</button
		>
	{/if}
</main>
