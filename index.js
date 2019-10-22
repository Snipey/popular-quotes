// Import Util Lib
const utils = require("./lib/utils")
const quoteObj = (quoteFile) =>{
  const quotes = require(`./data/${quoteFile}.json`)
  return {
    quotes: quotes,
    getRandom: ()=>utils.getRandom(quotes),
    listAll: ()=>utils.listAll(quotes),
    getByYear: (start,end,order)=>utils.getByYear(quotes,start,end,order)
  }
}
module.exports = {
  Movies: quoteObj('movies'),
  Tv: quoteObj('tv'),
  Speeches: quoteObj('speeches'),
  Books: quoteObj('books'),
  Anime: quoteObj('anime'),
  Lyrics: quoteObj('lyrics'),
  Sports:quoteObj('sports')
}