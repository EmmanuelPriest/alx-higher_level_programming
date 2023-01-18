#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie
*/

// Importing the request module
const request = require('request');

// Creating the first argument of the Movie ID object
const movieId = process.argv[2];

// Creating the Star Wars API URL endpoints
const starWarsApiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Using the request module to access the Star Wars API URL
request.get(starWarsApiUrl, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const starWars = JSON.parse(body); // Creating the JSON file
  const characters = starWars.characters;
  for (const character of characters) {
    request.get(character, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charStarWars = JSON.parse(body);
      console.log(charStarWars.name); // Displaying all characters
    });
  }
});
