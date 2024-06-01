<script lang="ts">
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Button, { Label } from '@smui/button';
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
				<Header class="color3">Video Game Consoles</Header>
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
				<Header class="color3">Graphic Cards</Header>
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
