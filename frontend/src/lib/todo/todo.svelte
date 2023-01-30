<script>
	export let task;
	import Edit from './edit.svelte';
	import Delete from './delete.svelte';
	import Done from './done.svelte';

	function formatDate(date) {
		const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
		return new Date(date).toLocaleDateString('it-IT', options);
	}
</script>

<main>
	<div class="card w-80 h-fit bg-neutral text-neutral-content">
		<div class="card-body items-center text-center">
			<h2 class="text-3xl truncate">{task.titolo}</h2>
			<h3 class="text-sm">{task.contenuto}</h3>
			<p class="text-xs">Due to: {formatDate(task.data)}</p>
			<div class="card-actions justify-end">
				<Delete {task} />
				<Edit {task} />
				<Done {task} />
			</div>
		</div>
	</div>
</main>
