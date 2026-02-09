import type { PageLoad } from "./$types";

export type Task = {
    id: number
    title: string,
    is_completed: string
}

type TaskResponse = {
    tasks: Task[]
}

export const load: PageLoad = async({ fetch }) => {
    const res = await fetch("http://localhost:8000/tasks")
    const data: TaskResponse = await res.json()
    console.log(data)
    return { tasks: data.tasks }
}