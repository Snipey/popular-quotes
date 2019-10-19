const movie = require('./data/movies.json');
const tv = require('./data/tv.json');
const speeches = require('./data/speeches.json');
const books = require('./data/books.json');
const anime = require('./data/anime.json');
const lyrics = require('./data/lyrics.json');

// Import Util Lib
const utils = require("./lib/utils")

const quoteObj = (quotes) =>{
  return {
    quotes: quotes,
    getRandom: ()=>utils.getRandom(quotes),
    listAll: ()=>utils.listAll(quotes),
    getByYear: (start,end,order)=>utils.getByYear(quotes,start,end,order)
  }
}
module.exports = {
  Movies: quoteObj(movie),
  Tv: quoteObj(tv),
  Speeches: quoteObj(speeches),
  Books: quoteObj(books),
  Anime: quoteObj(anime),
  Lyrics: quoteObj(lyrics)
}