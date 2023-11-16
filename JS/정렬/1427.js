let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("")


input.sort((x, y) => y - x);

console.log(input.join(""));