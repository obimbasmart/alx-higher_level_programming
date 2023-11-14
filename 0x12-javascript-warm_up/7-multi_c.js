#!/usr/bin/node

let nprint = Math.floor(process.argv[2]);
if (Number.isNaN(nprint)) {
  console.log('Missing number of occurrences');
}

while (nprint > 0) {
  console.log('C is fun');
  nprint--;
}
