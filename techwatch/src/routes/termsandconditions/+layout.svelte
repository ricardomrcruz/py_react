<script>
	/** @type {import('./$types').LayoutData} */
	export let data;
</script>

<h1>Settings</h1>

<div class="submenu">
	{#each data.sections as section}
		<p><a href="/termsandconditions/{section.slug}">{section.title}</a></p>
	{/each}
</div>

<slot></slot>
