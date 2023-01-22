#!/usr/bin/node
if (process.argv.length < 4) {
console.log('0');
} else {
const count = process.argv.slice(2);
count.sort((a, b) => b - a);
console.log(count[1]);
}
