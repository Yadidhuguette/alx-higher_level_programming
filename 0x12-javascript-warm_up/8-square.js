#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10))) {
console.log('Missing size');
} else {
let (n = 0; n < process.argv[2]; n++) {
console.log('X'.repeat(process.argv[2]));
}
}
