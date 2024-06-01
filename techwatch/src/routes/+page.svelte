<script lang="ts">
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Button, { Label } from '@smui/button';

	let clicked = 0;
</script>

<div class="flex justify-between">
	<div class="w-1/2">
		<h1 class="my-[150px] text-4xl">
			Track your favorite electronics prices and deals in real time with our surveillance services.
		</h1>
	</div>

	<div class="w-1/2"></div>
</div>

<div>
	<div class="accordion-container w-80">
		<Accordion multiple>
			<Panel>
				<Header class="color3">Top 2024 Electronics</Header>
				<Content>
					<ul>
						<li>
							<Button class="myClass">
								<Label>Apple Vision Pro</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>iPhone 15 Pro</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>iPhone 15 Pro Max</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Samsung Galaxy S24 Ultra</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Google Pixel 8 Pro</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Microsoft Surface Pro 9</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Apple iPad Pro 2024</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Amazon Echo Show 15</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Sony WH-1000XM5 Headphones</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Bose QuietComfort II</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>DJI Mavic 3 Pro Drone</Label>
							</Button>
						</li>
						<li>
							<Button class="myClass">
								<Label>Fitbit Charge 6</Label>
							</Button>
						</li>
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header>Panel 2</Header>
				<Content>The content for panel 2.</Content>
			</Panel>
			<Panel>
				<Header>Panel 3</Header>
				<Content>
					The content for panel 3.
					<ul>
						<li>Some</li>
						<li>More</li>
						<li>List</li>
						<li>Items</li>
						<li>To</li>
						<li>Show</li>
						<li>Big</li>
						<li>Height</li>
					</ul>
				</Content>
			</Panel>
			<Panel>
				<Header>Panel 4</Header>
				<Content>The content for panel 4.</Content>
			</Panel>
		</Accordion>
	</div>
</div>

<style>
	/* example */
	* :global(.myClass) {
		color: #f7f0e9 ;
		font-weight: lighter;
		text-transform: capitalize;
		font-family: 'JetBrains Mono', monospace;
	}
</style>
