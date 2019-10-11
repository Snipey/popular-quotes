const quotes = require('../data/lyrics.json');

const getByYear = (start, end, order) => {
  const list = quotes.filter((q) => q.year && q.year > start && q.year < end);
  if (order === "ascend") {
    return list.sort((a, b) => {
      if (a.year === b.year) {
        return 0;
      } else if (a.year > b.year) {
        return 1;
      } else {
        return -1;
      }
    });
  } else {
    return list;
  }
};

const getRandom = () => {
  const randNum = Math.floor(Math.random() * quotes.length);
  return quotes[parseInt(randNum, 10)].quote;
};

const listAll = () => {
  return quotes;
};

module.exports = {
  listAll,
  getRandom,
  getByYear
};
