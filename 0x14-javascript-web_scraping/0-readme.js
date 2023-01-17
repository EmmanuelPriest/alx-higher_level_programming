#!/usr/bin/node
/*
Script that reads and prints the content of a file
*/

const fs = require('fs');
const path = require('path');

const filePath = process.argv[2];
const encoding = 'utf-8';

fs.readFile(path.resolve(filePath), encoding, (err, data) => {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
