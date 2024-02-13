#!/usr/bin/node

const squireSize = Math.floor(Number(process.argv[2]));
if (isNaN(squireSize)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < squireSize; r++) {
    let row = '';
    for (let c = 0; c < squireSize; c++) row += 'X';
    console.log(row);
  }
}
