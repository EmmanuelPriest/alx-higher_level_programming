#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argc = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort((x, y) => x - y);
  console.log(argc[argc.length - 2]);
}
