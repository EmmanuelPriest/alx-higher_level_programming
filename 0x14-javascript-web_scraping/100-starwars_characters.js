#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie
*/

const request = require('request');

const movieId = process.argv[2];
const starWarsApiUrl = `https://swapi.dev/api/films/${movieId}/`;
// const starWarsApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(starWarsApiUrl, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const starWars = JSON.parse(body);
  const characters = starWars.characters;
  for (const character of characters) {
    request.get(character, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charStarWars = JSON.parse(body);
      console.log(charStarWars.name);
    });
  }
});
