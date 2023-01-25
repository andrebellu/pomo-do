<script>
    import { todos } from "../../store.js";
    import Todo from "$lib/Todo.svelte";
    import BackBtn from "$lib/BackBtn.svelte";

    import { fly, fade } from "svelte/transition";
</script>

<main in:fly={{ y: 200, duration: 1000, delay: 500 }} out:fade>
    <div class="flex justify-center items-center align-middle">
        <BackBtn />
        <h1 class="text-4xl px-2 text-center text-white">Done</h1>
    </div>
    <div class="flex flex-wrap justify-center items-center">
        {#each $todos as todo, pos}
            {#if todo[4] === 1}
                <Todo {todo} {pos} />
            {/if}
        {/each}
    </div>
</main>
