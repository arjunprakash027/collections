<script>
	export let name;
	import {count} from './func.svelte'
	export function increment() {
    count += 1
}
</script>

<main>
	<h1>Hello {name}!</h1>
	<button on:click={increment}>+</button>
	<p>{count}</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>