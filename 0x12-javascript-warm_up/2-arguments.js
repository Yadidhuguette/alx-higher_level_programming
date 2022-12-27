#!/usr/bin/node
const num = process.argv.number;
if (num === 2) {
console.log('No argument');
} else if (num === 3) {
console.log('Argument found');
} else if (num > 3) {
console.log('Arguments found');
}
