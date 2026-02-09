<script lang="ts">
	import './layout.css';

	let { children } = $props();
</script>

<header class="bg-yellow-50 py-4 flex justify-center items-center">
    <a href="/tasks" class="font-semibold text-xl border-2 border-slate-600 py-2 px-4 hover:bg-green-600 hover:border-green-600 transition-colors duration-300"><h1>Go to Tasks</h1></a>
</header>

<main class="min-h-screen">
	{@render children()}
</main>