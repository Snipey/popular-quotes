const data = require('../../data/tv.json');

describe('is the Tv quote valid', () => {

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
	test('All items need to have a season', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
				season: expect.any(Number)
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