<script>
	export let task;
	import { todos, url } from '../../store.js';

	function formatDate(date) {
		const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
		return new Date(date).toLocaleDateString('it-IT', options);
	}

	async function deleteTodo(id) {
		const options = {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json'
			}
		};

		const response = await fetch(url + '/' + id, options);
		const data = await response.json();
		await refresh();
	}

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
	<div class="card w-80 h-fit p-0 bg-neutral text-neutral-content">
		<div class="card-body items-center text-center">
			<h2 class="text-3xl truncate">{task.titolo}</h2>
			<h3 class="text-sm">{task.contenuto}</h3>
			<p class="text-xs">Due to: {formatDate(task.data)}</p>
			<div class="card-actions justify-end">
				<button
					class="btn btn-ghost btn-circle material-symbols-outlined text-xl"
					on:click={() => deleteTodo(task.id)}>delete</button
				>
				<button class="btn btn-ghost btn-circle material-symbols-outlined text-xl">edit</button>
				<button
					class="btn btn-primary btn-circle material-symbols-outlined text-xl"
					on:click={() => doneTodo(task.id)}>done</button
				>
			</div>
		</div>
	</div>
</main>
