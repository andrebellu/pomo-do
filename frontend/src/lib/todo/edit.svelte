<script>
	import { todos, url } from '../../store';
	export let task;

	async function editTodo() {
		const body = {
			titolo: task.titolo,
			contenuto: task.contenuto,
			data: task.data,
			stato: task.stato
		};

		const options = {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		};

		const response = await fetch(url + '/' + task.id, options);
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
	<label class="btn btn-ghost btn-circle material-symbols-outlined text-xl" for="edit">edit</label>

	<input type="checkbox" id="edit" class="modal-toggle" />

	<div class="modal modal-bottom sm:modal-middle">
		<div class="modal-box">
			<h1 class="text-3xl mb-3">Add Todo!</h1>
			<h3 class="font-bold text-lg">Add a title</h3>
			<input
				type="text"
				class="input input-bordered w-full mb-3"
				placeholder="Title"
				bind:value={task.titolo}
			/>

			<h3 class="font-bold text-lg">Add a description</h3>
			<input
				type="text"
				class="input input-bordered w-full mb-3"
				placeholder="Description"
				bind:value={task.contenuto}
			/>

			<h3 class="font-bold text-lg">Select a deadline</h3>
			<input
				type="date"
				class="input input-bordered w-full mb-3"
				placeholder="Date"
				bind:value={task.data}
				min={new Date().toISOString().split('T')[0]}
			/>
			<div class="modal-action">
				<label for="edit" class="btn btn-outline material-symbols-outlined">undo</label>
				<label
					for="edit"
					class="btn material-symbols-outlined btn-primary"
					on:click={editTodo}
					on:keypress={editTodo}>edit</label
				>
			</div>
		</div>
	</div>
</main>
