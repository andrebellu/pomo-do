<script>
  import { todos } from "../store";
  import Todo from "./Todo.svelte";

  let todoTitle = "";
  let todoDescription = "";
  let date = "";

  let filled = false;

  function addTodo() {
    let endpoint_add = "http://127.0.0.1:5000/tasks";
    let body = {
      titolo: todoTitle,
      contenuto: todoDescription,
      data: "2023-12-12",
      stato: 0,
    };

    const options = {
      method: "POST",
      body: JSON.stringify(body),
      headers: {
        "Content-Type": "application/json",
      },
    };

    fetch(endpoint_add, options).then((response) => response.json());
  }

  function checkFilled() {
    if (todoTitle.length > 0) {
      filled = true;
    } else {
      filled = false;
    }
  }

  function clear() {
    todoTitle = "";
    todoDescription = "";
    filled = false;
  }
</script>

<div class="flex items-center justify-center max-h-screen">
  <input
    type="text"
    bind:value={todoTitle}
    on:change={checkFilled}
    class="input input-primary mx-3"
    placeholder="Add Title"
  />

  <label class="btn btn-outline" for="my-modal-6">Add</label>
  <a
    class="text-white btn bg-info material-symbols-outlined rounded-full ml-3 hover:bg-blue-300 transition-all duration-300 ease-in-out"
    aria-hidden="true"
    href="/done">task_alt</a
  >

  <input type="checkbox" id="my-modal-6" class="modal-toggle" />
  <div class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <h3 class="font-bold text-lg text-center">
        Add a description if you want!<br /> Leave it blank if you don't.
      </h3>
      <div class="modal-action flex-col justify-center gap-y-3">
        <div class="btns gap-x-2 flex justify-center">
          <input
            type="text"
            bind:value={todoDescription}
            class="input input-primary"
            placeholder="Add a description"
          />

          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <label for="my-modal-6" class="btn btn-error" on:click={clear}
            ><span class="material-symbols-outlined"> close </span></label
          >
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <label for="my-modal-6" class="btn btn-primary" on:click={addTodo}
            ><span class="material-symbols-outlined text-black">
              done
            </span></label
          >
        </div>
        <input
          type="date"
          class="input input-bordered input-primary w-full input-xs"
        />
      </div>
    </div>
  </div>
</div>
