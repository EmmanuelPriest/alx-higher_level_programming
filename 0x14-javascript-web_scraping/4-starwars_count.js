#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present
*/

const request = require('request');
const starWarsApiUrl = process.argv[2];
// const starWarsApiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

let movieCounter = 0;

request(starWarsApiUrl, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  const movies = JSON.parse(body).results;
  movies.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.includes(`/${characterId}/`)) {
        movieCounter += 1;
      }
    });
  });
  console.log(`${movieCounter}`);
});
