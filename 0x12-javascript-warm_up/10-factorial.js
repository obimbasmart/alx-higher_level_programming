#!/usr/bin/node
// compute factorial of a num

function factorial (num) {
  if (Number.isNaN(num) || num === 0) {
    return 1;
  }

  return num * factorial(num - 1);
}

const arg1 = Math.floor(process.argv[2]);
console.log(factorial(arg1));
