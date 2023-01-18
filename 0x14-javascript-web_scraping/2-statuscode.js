#!/usr/bin/node
/*
Script that display the status code of a GET request
*/

// Importing the request module
const request = require('request');

// Creating the first URL argument to request based on index
const url = process.argv[2];

// Making a GET request
request.get(url, (error, res) => {
  if (error) {
    return console.log(error);
  }
  console.log(`code: ${res.statusCode}`); // Printing the status code
});
