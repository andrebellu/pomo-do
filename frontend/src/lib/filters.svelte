<script>
	import { todos, tomorrow } from '../store.js';

	let isActive = {
		dDate: false,
		aDate: true,
		tomorrow: false
	};

	function dDate() {
		clearActive();
		isActive.dDate = !isActive.dDate;

		todos.update((todos) => {
			todos.sort((a, b) => {
				return new Date(b.data) - new Date(a.data);
			});
			return todos;
		});
	}

	function aDate() {
		clearActive();
		isActive.aDate = !isActive.aDate;

		todos.update((todos) => {
			todos.sort((a, b) => {
				return new Date(a.data) - new Date(b.data);
			});
			return todos;
		});
	}

	function t() {
		clearActive();
		isActive.tomorrow = !isActive.tomorrow;

		tomorrow.set(!$tomorrow);
	}

	function clearActive() {
		isActive.dDate = false;
		isActive.aDate = false;
		isActive.tomorrow = false;
		tomorrow.set(false);
	}
</script>

<main>
	<div class="w-full align-middle flex my-5 gap-2 justify-center">
		<button
			class="badge badge-success badge-outline hover:bg-success hover:text-white cursor-pointer"
			on:click={aDate}
			class:active-badge={isActive.aDate}
		>
			<span class="material-symbols-outlined text-sm">arrow_upward</span> Date
		</button>
		<button
			class="badge badge-success badge-outline hover:bg-success hover:text-white cursor-pointer"
			on:click={dDate}
			class:active-badge={isActive.dDate}
		>
			<span class="material-symbols-outlined text-sm">arrow_downward</span> Date
		</button>
		<button
			class="badge badge-success badge-outline text-sm hover:bg-success hover:text-white cursor-pointer"
			on:click={t}
			class:active-badge={isActive.tomorrow}
		>
			Tomorrow
		</button>
	</div>
</main>
