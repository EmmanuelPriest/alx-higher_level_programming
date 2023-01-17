#!/usr/bin/node
/*
script that prints the title of a Star Wars movie where the episode number matches a given integer
*/

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log(body.title);
});
