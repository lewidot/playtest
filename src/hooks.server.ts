import type { Handle, ServerInit } from '@sveltejs/kit';
import log from '$lib/logger';
import * as fs from 'fs';

export const init: ServerInit = async () => {
	// Check if a playwright project is in the './tmp' directory.
	const tmpDirPath = './tmp';
	const tmpDir = fs.readdirSync(tmpDirPath);

	if (tmpDir.length === 0) {
		console.error('error: playwright project required in the tmp/ directory');
		process.exit(1);
	}
};

export const handle: Handle = async ({ event, resolve }) => {
	const response = await resolve(event);
	log.info(
		{ route: event.route.id, method: event.request.method, status: response.status },
		'request'
	);
	return response;
};
