// https://www.acmicpc.net/problem/2752

let fs = require("fs");
let input = fs.readFileSync("../input.txt").toString().split(" ");

let arr = input.map((x) => Number(x));

arr.sort((x, y) => x - y);

console.log(arr.join(" "));
