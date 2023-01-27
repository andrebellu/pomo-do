<script>
	export let task;

	function formatDate(date) {
		const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
		return new Date(date).toLocaleDateString(undefined, options);
	}
</script>

<main>
	<div class="card w-80 h-fit p-0 bg-neutral text-neutral-content">
		<div class="card-body items-center text-center">
			<h2 class="text-3xl">{task.contenuto}</h2>
			<h3 class="text-sm">{task.titolo}</h3>
			<p class="text-xs">Due to: {formatDate(task.data)}</p>
			<div class="card-actions justify-end">
				<button class="btn btn-ghost btn-circle material-symbols-outlined text-xl">delete</button>
				<button class="btn btn-ghost btn-circle material-symbols-outlined text-xl">edit</button>
				<button class="btn btn-primary btn-circle material-symbols-outlined text-xl">done</button>
			</div>
		</div>
	</div>
</main>
