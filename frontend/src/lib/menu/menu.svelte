<script>
	import { fly } from 'svelte/transition';
</script>

<main>
	<div class="menu flex items-center gap-8 relative">
		<div class="item todo-list" transition:fly={{ x: 100, duration: 400 }}>
			<h1 class="element text-4xl text-white">Todo List</h1>
		</div>

		<div class="item pomodoro" transition:fly={{ x: -100, duration: 500 }}>
			<h1 class="element text-4xl text-white">Pomodoro</h1>
		</div>

		<div class="item statistics" transition:fly={{ x: 100, duration: 600 }}>
			<h1 class="element text-4xl text-white">Statistics</h1>
		</div>
	</div>
</main>
