
let quotes = require('../data/tv.json');

const numGen = () => {
    return Math.floor(Math.random() * quotes.length);
};

const getByYear = (start, end) => {
    let list = [];
    quotes.forEach(item => {
        if (item.year && item.year > start && item.year < end) {
            list.push(item);
        }
	});
    return list.sort((a, b) => 
        a.year > b.year ? 1 : b.year > a.year ? -1 : 0	
    );
};

const getRandom = () => {
    let rand = numGen();

    return quotes[rand].quote;
};

const listAll = () => {
    return quotes;
};

module.exports = {
    listAll,
    getRandom,
    getByYear
};