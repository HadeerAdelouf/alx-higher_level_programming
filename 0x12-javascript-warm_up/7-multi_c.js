#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('c is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
