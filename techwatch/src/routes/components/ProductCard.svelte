<script lang="ts">
	import Button, { Label } from '@smui/button';
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import Card, {
		PrimaryAction,
		Media,
		MediaContent,
		Actions,
		ActionButtons,
		ActionIcons
	} from '@smui/card';

	import IconButton, { Icon } from '@smui/icon-button';


	let clicked = 0;

	export let title: string;
	export let price: string;
	export let description: string;
	export let link: string;
	export let img: string;

	// console.log('ProductCard Props:', { title, price, description, link, img }); // Debug log
</script>

<div class="card-container w-[95%] m-auto my-4">
	<Card class="bgcolor4  ">
		<PrimaryAction on:click={() => clicked++}>
			<div class="flex w-full m-5">
				<div class="card-media-container" style="background-image: url({img});"></div>
				<div class="mx-2">
					<Content class="mdc-typography--body2 mx-5">
						<h2
							class="mdc-typography--headline6 font-bold color3 truncate-text2"
							style="margin: 0;"
						>
							{title}
						</h2>
						<div class="flex w-full">
							<div>
								<h3 class="mdc-typography--subtitle2" style="margin: 0 0 10px; color: #888;">
									{price} $
								</h3>
							</div>
							<div class="m-3 color3 float-end">
								<h2>website</h2>
							</div>
						</div>
						<h2 class="truncate-text text-gray-500">{description}</h2>
					</Content>
				</div>
			</div>
		</PrimaryAction>
		<Actions>
			<ActionButtons>
				<Button on:click={() => clicked++}>
					<Label>
						<a href={link}>Check Product</a></Label
					>
				</Button>
				<!-- <Button on:click={() => clicked++}>
                    <Label>Another</Label>
                </Button> -->
			</ActionButtons>
			<ActionIcons>
				<IconButton
					on:click={() => clicked++}
					toggle
					aria-label="Add to favorites"
					title="Add to favorites"
				>
					<Icon class="material-icons" on>favorite</Icon>
					<Icon class="material-icons">favorite_border</Icon>
				</IconButton>
				<!-- <IconButton class="material-icons" on:click={() => clicked++} title="Share"
                    >share</IconButton
                > -->
				<IconButton class="material-icons" on:click={() => clicked++} title="More options"
					>more_vert</IconButton
				>
			</ActionIcons>
		</Actions>
	</Card>
</div>

<style>
	* :global(.card-media-container) {
		width: 35%;
		height: 200px;
		background-size: cover;
		background-position: center;
		flex-shrink: 0;
		border-radius: calc(var(--radius) - 4px);
	}

	* :global(.truncate-text) {
		display: -webkit-box;
		-webkit-line-clamp: 5;
		-webkit-box-orient: vertical;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	* :global(.truncate-text2) {
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	* :global(.mdc-typography--subtitle2) {
		color: #f7f0e9 !important;
		font-size: 3vh;
	}
</style>
