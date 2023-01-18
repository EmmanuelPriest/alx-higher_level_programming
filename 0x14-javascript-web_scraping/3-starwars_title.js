#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie where the episode number matches a given integer
*/

// Importing the request module
const request = require('request');

// Creating the first argument of the movie ID based on index
const movieId = process.argv[2];

// Creating the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Using the request module to make request to the Star Wars API
request(url, { json: true }, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log(body.title); // Printing of the Star Wars movie tiltle
});
