<script>
 let name = 'Budy';
 let angka = 0;
 function increment() {
	 angka += 1;
 }
 function reset() {
	 angka = 0;
 }
 function min() {
	 angka -= 1;
 }
 $: sum = angka * 2;
</script>
<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<p>Number Click! = {angka} <button on:click={increment}>Tambah</button><br><button on:click={reset}>Reset</button><br><button on:click={min}>Mines</button></p>
	<p>Hasil = {sum}</p>
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