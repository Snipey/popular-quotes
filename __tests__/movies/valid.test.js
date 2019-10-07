const data = require('../../data/movies.json');

describe('is the Movie quote valid', () => {
	test('All items need to have a year', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  year: expect.any(Number)
			});
		});
	});
	
	test('All items need to have a title', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  title: expect.any(String)
			});
		});
	});

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
			  character: expect.any(String)
			});
		});
	});
	test('All items need to have a actor', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  actor: expect.any(String)
			});
		});
	});
});