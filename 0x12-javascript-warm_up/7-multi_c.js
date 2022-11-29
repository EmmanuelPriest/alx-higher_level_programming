#!/usr/bin/node

const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < x; n++) {
    console.log('C is fun');
  }
}
