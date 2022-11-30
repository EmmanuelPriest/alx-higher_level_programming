#!/usr/bin/node

/* returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let n = 0; n < list.length; n++) {
    if (list[n] === searchElement) {
      count++;
    }
  }
  return (count);
};
