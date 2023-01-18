#!/usr/bin/node
/*
Script that reads and prints the content of a file
*/

// Importing the fs module for reading from and writing to file
const fs = require('fs');

// Creating the first argument based in index
const filePath = process.argv[2];
const encoding = 'utf-8';

// Using the fs module to read the file
fs.readFile(filePath, encoding, (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data); // printing the error object
});
