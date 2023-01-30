<script>
	export let task;
	import { todos, url } from '../../store';

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

	async function refresh() {
		const response = await fetch(url);
		const data = await response.json();
		todos.set(data);
	}
</script>

<main>
	<label for="delete" class="btn btn-ghost btn-circle material-symbols-outlined text-xl"
		>delete</label
	>

	<input type="checkbox" id="delete" class="modal-toggle" />
	<div class="modal modal-bottom sm:modal-middle">
		<div class="modal-box">
			<h3 class="font-bold text-lg">Delete Todo!</h3>
			<p class="py-4">Are you sure you want to delete this todo?</p>
			<div class="modal-action">
				<label for="delete" class="btn btn-primary">No</label>
				<label
					for="delete"
					class="btn"
					on:click={() => deleteTodo(task.id)}
					on:keypress={() => deleteTodo(task.id)}>Yes</label
				>
			</div>
		</div>
	</div>
</main>
