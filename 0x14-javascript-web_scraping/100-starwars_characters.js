#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie
*/

const request = require('request');
const movieId = process.argv[2];
//const starWarsApiUrl = `https://swapi.dev/api/films/${movieId}/`;
const starWarsApiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(starWarsApiUrl, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const starWars = JSON.parse(body);
    const characters = starWars.characters;
    characters.forEach(function (character) {
      request(character, function (error, res, body) {
        if (error) {
          console.log(error);
        } else {
          const charStarWars = JSON.parse(body);
          console.log(charStarWars.name);
        }
      });
    });
  }
});
