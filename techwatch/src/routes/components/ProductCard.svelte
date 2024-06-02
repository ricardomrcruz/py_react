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

	let description =
		'The PS5 Digital Edition unleashes new gaming possibilities that you never anticipated. Experience lightning fast loading with an ultra-high speed SSD, deeper immersion with support for haptic feedback, adaptive triggers, and 3D Audio, and an all-new generation of incredible PlayStation games. PS5 Digital Edition is an all-digital version of the PS5 console with no disc drive. Sign into your account for PlayStation Network and go to PlayStation Store to buy and download games.';

	let clicked = 0;
</script>

<div class="card-container w-[95%] m-auto my-4">
	<Card class="bgcolor4  ">
		<PrimaryAction on:click={() => clicked++}>
			<div class="flex w-full m-5">
				<div
					class="card-media-container"
					style="background-image: url({'https://c.media-amazon.com/images/I/61loOpDhuML._AC_UY218_.jpg'});"
				></div>
				<div class="mx-2">
					<Content class="mdc-typography--body2 mx-5">
						<h2 class="mdc-typography--headline6 font-bold color3" style="margin: 0;">
							PlayStation 5 Digital Edition - CFI-1102B
						</h2>
						<div class="flex w-full">
							<div>
								<h3 class="mdc-typography--subtitle2" style="margin: 0 0 10px; color: #888;">
									539.00 $
								</h3>
							</div>
							<div class="m-3 color3 float-end">
								<h2 >amazon</h2>
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
					<Label>Check Product</Label>
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
	* :global(.card-media-16x9) {
		background-image: url(https://c.media-amazon.com/images/I/61loOpDhuML._AC_UY218_.jpg);
	}

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
	* :global(.mdc-typography--subtitle2) {
		color: #f7f0e9 !important;
		font-size: 3vh;
	}
</style>
