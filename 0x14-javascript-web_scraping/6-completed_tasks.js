#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, res, body) => {
  if (err) return console.log(err);
  const dict = {};
  JSON.parse(body).forEach(task => {
    const id = task.userId;
    if (task.completed) {
      dict[id] = dict[id] ? dict[id] + 1 : 1;
    }
  });
  console.log(dict);
});
