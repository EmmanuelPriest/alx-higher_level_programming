#!/usr/bin/node

const x = process.argv[2];
const y = process.argv[3];
const func = function add(x, y) {
  return (parseInt(x) + parseInt(y));
}
