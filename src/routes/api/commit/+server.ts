import { error, json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { git } from '$lib/git';

export const GET: RequestHandler = async () => {
	try {
		// Fetch the latest commit for the /tmp repository.
		const pull = await git.pull();

		const commit = await git.log();

		return json({ commit: commit.latest?.hash, message: commit.latest?.message });
	} catch (e) {
		error(400, `${e}`);
	}
};
