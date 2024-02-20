#!/usr/bin/node

const args = process.argv;
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + args[2], (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
