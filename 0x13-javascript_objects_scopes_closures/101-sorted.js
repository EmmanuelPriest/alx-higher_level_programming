#!/usr/bin/node

const dict = require('./101-data.js').dict;

const updateDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (updateDict[dict[occurences]] === undefined) {
    updateDict[dict[occurences]] = [occurences];
  } else {
    updateDict[dict[occurences]].push(occurences);
  }
});
console.log(updateDict);
