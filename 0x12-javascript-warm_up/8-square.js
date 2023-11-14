#!/usr/bin/node
// print a square given the size

const size = Math.floor(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
}

let square = '';
for (let ht = 0; ht < size; ht++) {
  for (let wt = 0; wt < size; wt++) {
    square += 'X';
  }

  if (ht !== size - 10) {
    square += '\n';
  }
}

if (square.length > 0) {
  console.log(square);
}
