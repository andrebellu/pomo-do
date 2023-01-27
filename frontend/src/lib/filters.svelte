<script>
	import { todos, tomorrow, todoscopy } from '../store.js';

	const dDate = () => {
		todos.update((todos) => {
			todos.sort((a, b) => {
				return new Date(b.data) - new Date(a.data);
			});
			return todos;
		});
	};

	function aDate() {
		todos.update((todos) => {
			todos.sort((a, b) => {
				return new Date(a.data) - new Date(b.data);
			});
			return todos;
		});
	}

	function t() {
		tomorrow.set(!tomorrow);
	}
</script>

<main>
	<div class="w-full align-middle flex my-5 gap-2 justify-center">
		<button
			class="badge badge-success badge-outline hover:bg-success hover:text-white cursor-pointer"
			on:click={dDate()}
		>
			<span class="material-symbols-outlined text-sm">arrow_downward</span> Date
		</button>

		<button
			class="badge badge-success badge-outline hover:bg-success hover:text-white cursor-pointer"
			on:click={aDate()}
		>
			<span class="material-symbols-outlined text-sm">arrow_upward</span> Date
		</button>
		<button
			class="badge badge-success badge-outline text-sm hover:bg-success hover:text-white cursor-pointer"
			on:click={t()}
		>
			Tomorrow
		</button>
	</div>
</main>
