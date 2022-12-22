#!/usr/bin/node
if (process.argv.length < 4) {
console.log(0);
} else {
const ordN = process.argv.slice(2).sort((a, b) => a - b);
console.log(ordN[ordN.length - 2]);
}
