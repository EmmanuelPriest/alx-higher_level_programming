#!/usr/bin/node
/*
Script that display the status code of a GET request
*/

const request = require('request');
const url = process.argv[2];

request.get(url, (error, res) => {
  if (error) {
    return console.log(error);
  }
  console.log(`code: ${res.statusCode}`);
});
