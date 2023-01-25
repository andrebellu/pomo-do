<script>
  import "../app.css";
  import Header from "../lib/Header.svelte";

  import { page } from "$app/stores";
</script>

<main>
  {#if $page.url.pathname !== "/login"}
    <Header />
  {/if}

  <slot />
</main>

<style>
</style>
