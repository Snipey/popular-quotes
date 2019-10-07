const data = require('../../data/books.json');

describe('is the Book quote valid', () => {
	test('All items need to have a year', () => {
		data.forEach((years) => {
			expect(years).toMatchSnapshot({
			  year: expect.any(Number)
			});
		});
	});
	
	test('All items need to have a title', () => {
		data.forEach((titles) => {
			expect(titles).toMatchSnapshot({
			  title: expect.any(String)
			});
		});
	});
	
	test('All items need to have a author', () => {
		data.forEach((authors) => {
			expect(authors).toMatchSnapshot({
			  author: expect.any(String)
			});
		});
	});

	test('All items need to have a character', () => {
		data.forEach((characters) => {
			expect(characters).toMatchSnapshot({
			  character: expect.any(String)
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