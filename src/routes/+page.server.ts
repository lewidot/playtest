import { git } from '$lib/git';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const latestCommit = await git.log();
	return {
		commit: latestCommit.latest?.hash,
		message: latestCommit.latest?.message
	};
};
