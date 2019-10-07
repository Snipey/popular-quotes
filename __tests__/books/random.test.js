const { getRandom } = require('../../types/books.js');

describe('get random quote', () => {
	test('should return random quote', () => {
		const quote1 = getRandom();
		const quote2 = getRandom();
		expect(quote1).not.toEqual(quote2);
	});
});