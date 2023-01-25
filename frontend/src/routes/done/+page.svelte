<script>
  import { dones } from "../../store";
  import Todo from "$lib/Todo.svelte";
  import BackBtn from "$lib/BackBtn.svelte";

  import { slide } from "svelte/transition";
</script>

<main transition:slide>
  <div class="flex justify-center items-center align-middle">
    <BackBtn />
    <h1 class="text-4xl px-2 text-center text-white">Done</h1>
  </div>
  <div class="flex flex-wrap justify-center items-center">
    {#each $dones as todo, pos}
      <Todo {todo} {pos} />
    {/each}
  </div>
</main>
