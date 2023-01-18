#!/usr/bin/node
/*
Script that writes a string to a file
*/

// Importing the fs module for reading from and writing to a file
const fs = require('fs');
const encoding = 'utf-8';

// Creating the first and second arguments based on index
const filePath = process.argv[2];
const stringToFile = process.argv[3];

// Using the fs module to write to the file
fs.writeFile(filePath, stringToFile, encoding, (err) => {
  if (err) {
    return console.error(err); // Printing the error object
  }
});
