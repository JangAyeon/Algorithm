//https://www.acmicpc.net/problem/11004

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(" ").map((x) => Number(x));
let arr = input[1].split(" ").map((x) => Number(x));

//console.log(n,k,arr)

arr.sort((x, y) => x - y);
console.log(arr[k - 1]);
