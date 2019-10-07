const { getRandom } = require('../../types/movies.js');

describe('get random quote', () => {
	test('should return random quote', () => {
		const quote1 = getRandom();
		const quote2 = getRandom();
		expect(quote1).not.toEqual(quote2);
	});
});