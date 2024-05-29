import { error } from '@sveltejs/kit';
/** @type {import('./$types').PageLoad} */ export function load({ params }) {
	if (params.slug === 'hello-world') {
		return {
			title: 'News',
			content: 'Keep yourself updated with the biggest price change news in the market.'
		};
	}
	error(404, 'Not found');
}
