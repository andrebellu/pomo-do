<script>
	import { todos, url } from '../store';

	let titolo = '';
	let contenuto = '';
	let data = '';
	let filled = false;

	function addTodo() {
		const body = {
			titolo: titolo,
			contenuto: contenuto,
			data: data,
			stato: 0
		};

		const options = {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		};

		fetch(url, options)
			.then((response) => response.json())
			.then((data) => {
				todos.update((old) => [...old, data]);
			});
	}
</script>

<div class="flex items-center justify-center max-h-screen">
	<label class="btn btn-outline w-32" for="my-modal-6">Add</label>
	<a
		class="text-white btn bg-info material-symbols-outlined rounded-full ml-3 hover:bg-blue-300 transition-all duration-300 ease-in-out"
		aria-hidden="true"
		href="/done">task_alt</a
	>
	<input type="checkbox" id="my-modal-6" class="modal-toggle" />

	<div class="modal modal-bottom sm:modal-middle">
		<div class="modal-box">
			<h1 class="text-3xl mb-3">Add Todo!</h1>
			<h3 class="font-bold text-lg">Add a title</h3>
			<input
				type="text"
				class="input input-bordered w-full mb-3"
				placeholder="Title"
				bind:value={titolo}
			/>

			<h3 class="font-bold text-lg">Add a description</h3>
			<input
				type="text"
				class="input input-bordered w-full mb-3"
				placeholder="Description"
				bind:value={contenuto}
			/>

			<h3 class="font-bold text-lg">Select a deadline</h3>
			<input
				type="date"
				class="input input-bordered w-full mb-3"
				placeholder="Date"
				bind:value={data}
			/>
			<div class="modal-action">
				<label for="my-modal-6" class="btn btn-outline material-symbols-outlined">undo</label>
				<label
					for="my-modal-6"
					class="btn material-symbols-outlined"
					on:click={addTodo}
					on:keypress={addTodo}>add</label
				>
			</div>
		</div>
	</div>
</div>
