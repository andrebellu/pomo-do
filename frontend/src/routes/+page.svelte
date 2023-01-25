<script>
  import Add from "../lib/Add.svelte";
  import Todo from "../lib/Todo.svelte";
  import { slide } from "svelte/transition";

  import { todos } from "../store.js";

  import { onMount } from "svelte";

  let endpoint_get = "http://127.0.0.1:5000/tasks";

  onMount(async () => {
    fetch(endpoint_get)
      .then((response) => response.json())
      .then((data) => {
        todos.set(data);
      });
  });
</script>

<main transition:slide>
  <Add />

  <div class="flex justify-center align-middle items-center flex-wrap">
    {#each $todos as todo, pos}
      {#if !todo.done}
        <Todo {todo} {pos} />
      {/if}
    {/each}
  </div>
</main>

<style>
</style>
