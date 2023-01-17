#!/usr/bin/node
/*
Script that gets the contents of a webpage and stores it in a file
*/

const request = require('request');
const fs = require('fs');
const requestUrl = process.argv[2];
const filePath = process.argv[3];
const encoding = 'utf-8';

request(requestUrl, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(filePath, body, { encoding }, (writeError) => {
    if (writeError) {
      return console.error(writeError);
    }
    console.log(`${filePath}`);
  });
});
