<script lang="ts">
	import { onMount } from 'svelte';

	import ProductNavAccordion from './components/ProductNavAccordion.svelte';
	import ProductCard from './components/ProductCard.svelte';

	interface Product {
		title: string;
		price: string;
		description: string;
		link: string;
		img: string;
	}

	let products: Product[] = [];
	let selectedCategory = 'playstation-5';
	let categories = ['playstation-5', 'iphone-15-pro'];


		async function fetchProducts(category: string) {
			try{
			const response = await fetch(`./${category}.json`);
			if (response.ok) {
				products = await response.json();
			} else {
				products = [];
			}
			} catch (error) {
				console.error('Failed to fetch prod:', error);
				products= [];
			}
		}

		
		function selectCategory(category:string){
			selectedCategory = category;
			fetchProducts(category);
		}
		
		onMount(() => {
			fetchProducts(selectedCategory);
		})
		
		// selectCategory('playstation-5');

	

</script>

<div class="flex justify-between">
	<div class="w-1/2">
		<h1 class="my-[140px] text-4xl">
			Track your favorite electronics prices and deals in real time with our surveillance services.
		</h1>
	</div>

	<div class="w-1/2"></div>
</div>

<div class="float-end">
	<h2>Last Price Update: 23 January 2024</h2>
</div>

<div class="flex w-full justify-between">
	<div class="w-[30%]">
		<ProductNavAccordion {categories} {selectCategory}/>
	</div>

	<div class=" w-[68%] float-end bgcolor5 mt-8 rounded-sm justify-center">
		{#each products as product}
			<ProductCard
				title={product.title}
				description={product.description}
				price={product.price}
				link={product.link}
				img={product.img}
			/>
		{/each}
	</div>
</div>

<!-- <pre class="status">Clicked: {clicked}</pre> -->
