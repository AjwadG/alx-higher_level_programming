#!/usr/bin/node

const args = process.argv;
const request = require('request');

main();

function getBody (value) {
  return new Promise((resolve, reject) => {
    request(value, (error, response, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body));
    });
  });
}

async function main () {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  let movie = await getBody(url);
  movie = movie.characters;
  for (let i = 0; i < movie.length; i++) {
    const name = await getBody(movie[i]);
    console.log(name.name);
  }
}
