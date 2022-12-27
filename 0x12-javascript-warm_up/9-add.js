#!/usr/bin/node
function add (a, b) {
return a + b;
}
console.log(add(Number(process.agrv[2]), Number(process.argv[3])));
