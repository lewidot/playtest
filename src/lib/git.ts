import { simpleGit, type SimpleGitOptions } from 'simple-git';

const options: Partial<SimpleGitOptions> = {
	baseDir: './tmp',
	binary: 'git',
	maxConcurrentProcesses: 6,
	trimmed: false
};

export const git = simpleGit(options);
