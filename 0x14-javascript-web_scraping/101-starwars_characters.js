#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie
*/

// Importing the request module
const request = require('request');

// Creating the first argument of the Movie ID object
const movieId = process.argv[2];

// Creating the Star Wars API URL
const starWarsUrl = `https://swapi.dev/api/films/${movieId}/`;

// Creating the empty character array to store the movie characters
let characters = [];

// using the request module to access the Star Wars API URL
request(starWarsUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const starWars = JSON.parse(body); // Creating the JSON file
  characters = starWars.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
