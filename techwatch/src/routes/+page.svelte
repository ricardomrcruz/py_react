<script lang="ts">
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Button, { Label } from '@smui/button';
	import ProductNavAccordion from './components/ProductNavAccordion.svelte';
</script>

<div class="flex justify-between">
	<div class="w-1/2">
		<h1 class="my-[140px] text-4xl">
			Track your favorite electronics prices and deals in real time with our surveillance services.
		</h1>
	</div>

	<div class="w-1/2"></div>
</div>

<div class="float-end mb-8">
	<h2>Last Price Update: 23 January 2024</h2>
</div>

<div class="flex w-full justify-between">
	<div class="w-[30%]">
		<ProductNavAccordion />
	</div>

	<div class=" w-[65%] float-end bgcolor5 mt-8 rounded-sm ">
		
	</div>
</div>
