<script lang="ts">
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Button, { Label } from '@smui/button';
	import ProductNavAccordion from './components/ProductNavAccordion.svelte';
	import ProductCard from './components/ProductCard.svelte';
	export let data;

	import Card, {
		PrimaryAction,
		Media,
		MediaContent,
		Actions,
		ActionButtons,
		ActionIcons
	} from '@smui/card';

	import IconButton, { Icon } from '@smui/icon-button';

	
	//  console.log('posts:', data); // Debug log
	

	let clicked = 0;
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
		<ProductNavAccordion />
	</div>

	<div class=" w-[68%] float-end bgcolor5 mt-8 rounded-sm justify-center">
		{#each data.posts1 as post}
			<ProductCard
				title={post.title}
				description={post.description}
				price={post.price}
				link={post.link}
				img={post.img}
			/>
		{/each}
		{#each data.posts2 as post}
			<ProductCard
				title={post.title}
				description={post.description}
				price={post.price}
				link={post.link}
				img={post.img}
			/>
		{/each}
		
	</div>
</div>

<pre class="status">Clicked: {clicked}</pre>
