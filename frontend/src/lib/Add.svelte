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
            data: "2021-05-01",
            stato: 0,
        };

        $todos = [...$todos, body];
        console.log($todos);

        const options = {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                "Content-Type": "application/json",
            },
        };

        fetch(endpoint_add, options).then((response) => response.json());

        clear();
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
    <label class="btn btn-outline w-32" for="my-modal-6">Add</label>
    <a
        class="text-white btn bg-info material-symbols-outlined rounded-full ml-3 hover:bg-blue-300 transition-all duration-300 ease-in-out"
        aria-hidden="true"
        href="/done">task_alt</a
    >
    <input type="checkbox" id="my-modal-6" class="modal-toggle" />

    <div class="modal modal-bottom sm:modal-middle">
        <div class="modal-box">
            <h1 class="text-3xl mb-3">Add Todo!</h1>
            <h3 class="font-bold text-lg">Add a title</h3>
            <input
                type="text"
                class="input input-bordered w-full mb-3"
                placeholder="Title"
                bind:value={todoTitle}
                on:input={checkFilled}
            />

            <h3 class="font-bold text-lg">Add a description</h3>
            <input
                type="text"
                class="input input-bordered w-full mb-3"
                placeholder="Description"
                bind:value={todoDescription}
            />

            <h3 class="font-bold text-lg">Select a deadline</h3>
            <input
                type="date"
                class="input input-bordered w-full mb-3"
                placeholder="Date"
                bind:value={date}
            />
            <div class="modal-action">
                <label
                    for="my-modal-6"
                    class="btn btn-outline material-symbols-outlined"
                    >undo</label
                >
                <label
                    for="my-modal-6"
                    class="btn material-symbols-outlined"
                    on:click={addTodo}
                    on:keypress={addTodo}>add</label
                >
            </div>
        </div>
    </div>
</div>
