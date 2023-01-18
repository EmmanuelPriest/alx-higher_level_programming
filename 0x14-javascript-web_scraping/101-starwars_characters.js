#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie
*/

const request = require('request');

const movieId = process.argv[2];
const starWarsUrl = `https://swapi.dev/api/films/${movieId}/`;
let characters = [];

request(starWarsUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const starWars = JSON.parse(body);
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
