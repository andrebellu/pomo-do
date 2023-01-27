import { writable } from "svelte/store";

export const todos = writable([]);

export const url = "http://127.0.0.1:5000/tasks"