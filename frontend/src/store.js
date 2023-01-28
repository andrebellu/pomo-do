import { writable } from "svelte/store";

export const todos = writable([]);

export const url = "http://192.168.0.101:5000/tasks"

export const tomorrow = writable(false);