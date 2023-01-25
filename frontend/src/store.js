import { writable, derived } from 'svelte/store';

export const todos = writable([]);

export const dones = derived(todos, $todos => $todos.filter(todo => todo.done));