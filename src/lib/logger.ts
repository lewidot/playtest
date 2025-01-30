import pino from 'pino';

const log = pino({
	formatters: {
		level: (label) => {
			return { level: label.toUpperCase() };
		},
		bindings: () => {
			return {};
		}
	},
	timestamp: pino.stdTimeFunctions.isoTime
});
export default log;
