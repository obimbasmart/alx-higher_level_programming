#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  process.argv.forEach((item, index) => {
    if (index < 2) {
      return;
    }

    console.log(item);
  });
}
