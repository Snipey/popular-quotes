const data = require('../../data/speeches.json');

describe('is the speech quote valid', () => {
	test('All items need to have a year', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  year: expect.any(Number || null)
			});
		});
	});
	
	test('All items need to have a person', () => {
		data.forEach((quotes) => {
			expect(quotes).toMatchSnapshot({
			  person: expect.any(String)
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