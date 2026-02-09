<script lang="ts">
	import { enhance } from "$app/forms";

    type InsertTask = {
        title: string
        is_completed: string | 'Pending'
    }


    async function addTask(task_data: InsertTask) {

        const res = await fetch('http://localhost:8000/tasks', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(task_data),
        })

        if (!res.ok) {
            console.log("Failed to add task")
            return
        }

        const result = await res.json();
        console.log("Task Added!", result)
        
    }

    function handleSubmit(event: SubmitEvent) {
        event.preventDefault();

        const form = event.currentTarget as HTMLFormElement;
        const formadata = new FormData(form);

        const task: InsertTask = {
            title: formadata.get("taskName") as string,
            is_completed: formadata.get("status") as string
        }

        addTask(task)
        form.reset();
    }

</script>

<div class="flex items-center justify-center flex-col">
    <h1 class="text-3xl py-3">Task List</h1>
    <form method="POST" action="" class="flex flex-col justify-between gap-4" onsubmit={handleSubmit}>
        <div class="form-fields">
            <label for="taskName"><input type="text" name="taskName" placeholder="Enter Task Title:" class="py-2 px-1"></label>
        </div>
        <div class="form-fields">
            <select name="status" id="status">
                <option value="Pending">Pending</option>
                <option value="Completed">Completed</option>
                <option value="Abandoned">Abandoned</option>
            </select>
        </div>
        <button type="submit" class="border bg-green-600 py-2 px-4 my-3">
            Add Task
        </button>
    </form>
    <a href="/tasks/list" type="button" class="border bg-green-600 py-2 px-4">
        <h1>Go to Task List</h1>
    </a>
</div>