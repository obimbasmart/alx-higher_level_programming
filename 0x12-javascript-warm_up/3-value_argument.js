#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  process.argv.forEach((item, index) => {
    if (index < 2) {
      return;
    }

    console.log(item);
  });
}
