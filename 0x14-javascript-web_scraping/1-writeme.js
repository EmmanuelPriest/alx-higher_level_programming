#!/usr/bin/node
/*
Script that writes a string to a file
*/
const fs = require('fs');
const encoding = 'utf-8';

const filePath = process.argv[2];
const stringToFile = process.argv[3];

fs.writeFile(filePath, stringToFile, encoding, (err) => {
  if (err) {
    return console.error(err);
  }
});
