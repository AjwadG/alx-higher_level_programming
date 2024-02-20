#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, (err, res, body) => {
  if (err) return console.log(err);
  JSON.parse(body).characters.forEach(chare => {
    request(chare, (error, response, boDy) => {
      if (error) return console.log(error);
      console.log(JSON.parse(boDy).name);
    });
  });
});
