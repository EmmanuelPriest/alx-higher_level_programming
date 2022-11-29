#!/usr/bin/node

const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let n = 0; n < x; n++) {
    /* let m = 0; */
    let mySquare = '';
    for (let m = 0; m < x; m++) {
      mySquare += 'X';
    }
    console.log(mySquare);
  }
}
