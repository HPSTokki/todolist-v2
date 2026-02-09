<script lang="ts">
	import type { PageData } from '../$types';
	import type { Task } from './+page';

	const { data } = $props<{ data: PageData }>();

	let tasks = $derived<Task[]>(data.tasks ?? [])

    async function deleteTask(id:number) {
        
        tasks = tasks.filter(task => task.id !== id);

        try {
            const res = await fetch(`http://localhost:8000/tasks/${id}`, {
                method: 'DELETE'
            })
            if (!res.ok) throw new Error('Delete Failed')
            const json = await res.json()
            console.log(json.message)
        } catch (error) {
            console.log(error)
        }

    }

</script>

<div class="flex flex-col items-center justify-center gap-3">
    <h1 class="text-3xl py-2">List of Tasks: </h1>
	{#if tasks.length === 0}
		<h1>No Tasks Yet!</h1>
	{:else}
		<ul>
			{#each tasks as task}
				<li>
					<strong>{task.title}</strong> - {task.is_completed}
                    <button onclick={() => deleteTask(task.id)}>Delete Task</button>
				</li>
			{/each}
		</ul>
	{/if}
</div>
