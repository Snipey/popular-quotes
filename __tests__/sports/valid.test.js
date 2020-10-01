const data = require('../../data/sports.json');

describe('is the Sports quote valid', () => {

	test('All items need to have a quote', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
				quote: expect.any(String)
			});
		});
	});
	test('All items need to have a character', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
				quote: expect.any(String)
			});
		});
	});
	test('All items need to have a Athlete', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
				athlete: expect.any(String)
			});
		});
	});
	test('All items need to have a year', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  year: expect.any(Number)
			});
		});
	});
});
