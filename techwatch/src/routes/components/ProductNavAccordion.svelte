<script lang="ts">
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Button, { Label } from '@smui/button';

	 export let categories: string[];
	 export let consoles: string[];
 	 export let selectCategory: (category:string)=> void;
</script>

<!-- <style>
    .myClass {
      color: #f7f0e9;
      font-weight: lighter;
      text-transform: capitalize;
      font-family: 'JetBrains Mono', monospace;
    }
  </style> -->

<div class="mt-8">
	<div class="accordion-container ">
		<Accordion multiple>
			<Panel>
				<Header class="color3">Top 2024 Electronics</Header>
				<Content>
					<ul>
						{#each categories as category}
							<li>
								<Button class="myClass" on:click={() => selectCategory(category)} >
									<Label>{category}</Label>
								</Button>
							</li>
						{/each}
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header class="color3">Video Game Consoles</Header>
				<Content>
					<ul>
						{#each consoles as console}
							<li>
								<Button class="myClass" on:click={() => selectCategory(console)} >
									<Label>{console}</Label>
								</Button>
							</li>
						{/each}
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header class="color3">Graphic Cards</Header>
				<Content>
					<ul>
						<li>
							<Button class="myClass">
								<Label>Playstation 4</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Playstation 5</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Xbox One</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Xbox Series X</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Xbox Series S</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Nintendo Switch</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Nintendo Switch OLED</Label>
							</Button>
						</li>
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header class="color3">Processors</Header>
				<Content>
					<ul>
						<li>
							<Button class="myClass">
								<Label>example</Label>
							</Button>
						</li>
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header class="color3">Motherboards</Header>
				<Content>
					<ul>
						<li>
							<Button class="myClass">
								<Label>example</Label>
							</Button>
						</li>
					</ul>
				</Content>
			</Panel>
		</Accordion>
	</div>
</div>

<style>
	* :global(.myClass) {
		color: #f7f0e9;
		font-weight: lighter;
		text-transform: capitalize;
		font-family: 'JetBrains Mono', monospace;
	}
</style>
