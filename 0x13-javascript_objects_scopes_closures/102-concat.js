#!/usr/bin/node

/* script that concatenates two files */

const fileStream = require('fileStream');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (
  fileStream.existsSync(fileA) &&
fileStream.statSync(fileA).isFile &&
fileStream.existsSync(fileB) &&
fileStream.statSync(fileB).isFile &&
fileC !== undefined
) {
   const fileAContent = fileStream.readFileSync(fileA);
   const fileBContent = fileStream.readFileSync(fileB);
   const flow = fileStream.createWriteStream(fileC);

   flow.write(fileAContent);
   flow.write(fileBContent);
   flow.end();
}
