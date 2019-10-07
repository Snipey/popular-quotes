const data = require('../../data/anime.json');

describe('is the Anime quote valid', () => {
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
	
	test('All items need to have a episode', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  episode: expect.any(Number)
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
});