let { Movies } = require('../../index.js');
expect.extend({
	toBeWithinRange(received, floor, ceiling) {
	  const pass = received >= floor && received <= ceiling;
	  if (pass) {
		return {
		  message: () =>
			`expected ${received} not to be within range ${floor} - ${ceiling}`,
		  pass: true,
		};
	  } else {
		return {
		  message: () =>
			`expected ${received} to be within range ${floor} - ${ceiling}`,
		  pass: false,
		};
	  }
	},
  });
describe('is the Movies quote random', () => {
	test('should return a random quote', () => {
		let quote1 = Movies.getRandom();
		let quote2 = Movies.getRandom();
		expect(quote1).not.toMatch(quote2);
	});
});
describe('does it get quotes by year', () => {
	test('should return a range of quotes by year', () => {
		let startYear = 2001;
		let endYear = 2004;
		let range = Movies.getByYear(startYear, endYear);
		range.forEach( item => {
			expect(item.year).toBeWithinRange(startYear, endYear);
		});
	});
});