<script>
    import Add from "../lib/Add.svelte";
    import Todo from "../lib/Todo.svelte";

    import { todos } from "../store.js";

    import { onMount } from "svelte";

    import { fly, fade } from "svelte/transition";

    let endpoint_get = "http://127.0.0.1:5000/tasks";

    onMount(async () => {
        fetch(endpoint_get)
            .then((response) => response.json())
            .then((data) => {
                todos.set(data);
            });
    });
</script>

<main in:fly={{ y: 200, duration: 1000, delay: 500 }} out:fade>
    <Add />

    <div class="flex justify-center align-middle items-center flex-wrap">
        {#each $todos as todo, pos}
            {#if todo[4] === 0}
                <Todo {todo} {pos} />
            {/if}
        {/each}
    </div>
</main>

<style>
</style>
