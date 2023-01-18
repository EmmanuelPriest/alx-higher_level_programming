#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present
*/

// Importing the request module
const request = require('request');

// Creating the first argument of the Star Wars API URL
const starWarsApiUrl = process.argv[2];

// Creating the character ID
const characterId = 18;

// Creating the counter for updating character ID
let movieCounter = 0;

// Using the request module o access the Star Wars API URL
request(starWarsApiUrl, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  const movies = JSON.parse(body).results; // Creating JSON file
  movies.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.includes(`/${characterId}/`)) {
        movieCounter += 1;
      }
    });
  });
  console.log(`${movieCounter}`); // Printing the no. of movies Wedge Anthile showed in
});
