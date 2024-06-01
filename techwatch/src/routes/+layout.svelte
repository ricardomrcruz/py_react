<script>
	import '../app.css';
</script>

<div class="layout">
	<nav class="flex justify-between">
		<div>
			<h1 class="text-[1.70rem] font-extralight"><a href="/" class="color3">Techwatch</a></h1>
		</div>
		<div class="flex space-x-4 pt-1">
			<p><a href="/about">About</a></p>
			<p><a href="/products">Products</a></p>
			<p><a href="/api">Api</a></p>
			<p>
				<a href="/register" class="bgcolor5 color3  p-2 ml-2 rounded-sm text-[1.15rem]">Register</a>
			</p>
		</div>
	</nav>

	<slot></slot>
</div>
