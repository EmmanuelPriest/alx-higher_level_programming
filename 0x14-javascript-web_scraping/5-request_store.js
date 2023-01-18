#!/usr/bin/node
/*
Script that gets the contents of a webpage and stores it in a file
*/

const request = require('request');
const fs = require('fs');
const requestUrl = process.argv[2];
const filePath = process.argv[3];
// const encoding = 'utf8';

request(requestUrl, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.log(writeError);
      }
    });
  }
});
