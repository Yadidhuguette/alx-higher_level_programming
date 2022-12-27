#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
for (let n = 0; n < size; n++) {
console.log('X'.repeat(size));
}
} else {
console.log('Missing size');
}
