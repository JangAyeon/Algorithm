let fs = require("fs")
let line = fs.readFileSync("./input.txt").toString().split("\n")

let [h,m]=line[0].split(" ").map(Number)
let gap = Number(line[1])

let time = h*60+m+gap

let hour = Math.floor(time/60)%24
let min = time%60

console.log(h,m,time,hour, min)