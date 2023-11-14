#!/usr/bin/node
// print the addition of two numbers

function add (a, b) {
  return (a + b);
}

const arg1 = Math.floor(process.argv[2]);
const arg2 = Math.floor(process.argv[3]);

console.log(add(arg1, arg2));
