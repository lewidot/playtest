import type { Handle } from '@sveltejs/kit';
import log from '$lib/logger';

export const handle: Handle = async ({ event, resolve }) => {
	const response = await resolve(event);
	log.info(
		{ route: event.route.id, method: event.request.method, status: response.status },
		'request'
	);
	return response;
};
