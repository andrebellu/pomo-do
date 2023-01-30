<script>
    import { onMount } from 'svelte';
    let done = 0;
    let total = 0;

    onMount(() => {
		fetch("http://127.0.0.1:5000/tasks/statistics")
			.then((response) => response.json())
			.then((data) => {
				done = data.done;
                total = data.total;
			});
	});

</script>
<h1 class="text-4xl text-center">Statistics</h1>
<div class="h-screen flex justify-center items-center">
    <div class="flex flex-col gap-5">
        <div class="flex justify-center">
            <div class="radial-progress bg-primary text-primary-content border-4 border-primary text-2xl" style="--value:{(done / total) * 100}; --size:20rem;">{(done / total) * 100}%</div>
        </div>
        <div class="flex justify-center">
            <p class="text-lg">Completed {done} on {total} task</p>
        </div>
    </div>
</div>
