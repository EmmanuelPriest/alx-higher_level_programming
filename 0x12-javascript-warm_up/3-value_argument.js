#!/usr/bin/node

const argc = process.argv;
console.log(argc);
argc.forEach((e, idx) => {
  if (idx === 0) {
    console.log(${e});
  }
}
