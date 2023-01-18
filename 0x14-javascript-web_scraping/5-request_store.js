#!/usr/bin/node
/*
Script that gets the contents of a webpage and stores it in a file
*/

// Import the request and fs modules
const request = require('request');
const fs = require('fs');

// Creating the first and second arguments for the URL request and file path repectively
const requestUrl = process.argv[2];
const filePath = process.argv[3];

// Using the request module to access the URL request and write to the file using fs module
request(requestUrl, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.log(writeError); // Displaying the error in the file
      }
    });
  }
});
