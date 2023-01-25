<script>
  import Hamburger from "../lib/Hamburger.svelte";
  import Menu from "../lib/Menu.svelte";
  import { fly, fade } from "svelte/transition";

  export let open = false;
  export let onClick = () => {
    open = !open;
  };
</script>

<main>
  <div class="navbar bg-invisible md:hidden mb-5">
    <Hamburger {open} {onClick} />
    <h1 class="text-4xl text-white">Pomodò</h1>
  </div>

  <div
    class="navbar bg-invisible hidden m-0 w-0 p-0 md:visible md:w-full md:flex md:justify-between md:mb-5"
  >
    <h1 class="text-4xl text-white mx-10">Pomodò</h1>
    <div class="flex gap-10 mx-10">
      <h1 class="text-2xl text-white element" href="/">Todos</h1>
      <h1 class="text-2xl text-white element">Pomodoro</h1>
      <h1 class="text-2xl text-white element">Statistics</h1>
    </div>
  </div>

  {#if open}
    <div
      class="page h-screen w-screen flex justify-center items-center bg-base-100 absolute z-50"
      transition:fade
    >
      <Menu />
    </div>
  {/if}
</main>
