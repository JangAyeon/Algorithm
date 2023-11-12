let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split(" ")
let h = parseInt(line[0])
let m = parseInt(line[1])

let total = h*60+m
total-=45

let hour = Math.floor(total/60)
let min = total%60

hour = hour<0? hour+24:hour
min = min<0? min+60:min
console.log(hour, min)