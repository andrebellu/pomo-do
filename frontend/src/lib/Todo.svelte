<script>
  import { todos } from "../store.js";

  export let todo = {};

  export let pos;

  function remove(id) {
    let endpoint_delete = "http://127.0.0.1:5000/tasks/" + id;
    const options = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    };

    fetch(endpoint_delete, options).then((response) => response.json());

    todos.update((old) => {
      old.splice(pos, 1);
      return old;
    });
  }

  function edit() {
    todos.update((old) => {
      old[pos].edit = !old[pos].edit;
      return old;
    });
  }

  function done() {
    todos.update((old) => {
      old[pos].done = !old[pos].done;
      return old;
    });
  }
</script>

<div class="card w-96 bg-neutral text-neutral-content m-5 z-10 relative">
  <div class="card-body items-center text-center flex-wrap">
    <h2 class="card-title">{todo[1]}</h2>
    <p>{todo[3]}</p>

    {#if todo[4] == 1}
      <div class="badge bg-green-500">
        <span class="text-black">Done</span>
      </div>
    {:else}
      <div class="badge bg-warning">
        <span class="text-black">Not Done</span>
      </div>
    {/if}

    <div class="card-actions justify-end">
      <div class="btn-group">
        <button
          class="btn btn-warning material-symbols-outlined"
          on:click={() => {
            remove(todo[0]);
          }}
        >
          delete
        </button>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-missing-attribute -->
        <a class="btn btn-primary material-symbols-outlined" on:click={edit}>
          edit
        </a>
        <button class="btn btn-primary" on:click={done}>Done</button>
      </div>
    </div>
  </div>
</div>
