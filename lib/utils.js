const numGen = () => {
    return Math.floor(Math.random() * quotes.length);
};

module.exports.getByYear = (quotes,start, end, order) => {
    let list = [];
    quotes.forEach(item => {
        if (item.year && item.year > start && item.year < end) {
            list.push(item);
        }
	});
	if(order === 'ascend'){
		return list.sort((a, b) => 
			a.year > b.year ? 1 : b.year > a.year ? -1 : 0	
		);
    }
    return list;
};

module.exports.getRandom = (quotes) => {
  const randNum = Math.floor(Math.random() * quotes.length);
  return quotes[parseInt(randNum, 10)].quote;
};

module.exports.listAll = (quotes) => {
    return quotes;
};