#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, res, body) => {
  if (err) return console.log(err);
  let count = 0;
  JSON.parse(body).results.forEach(movie => {
    movie.characters.forEach(chare => {
      if (chare.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
