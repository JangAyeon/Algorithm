let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(line[0])


function solution(arr, m){

  count=0
  while(arr.length!=0){
    let max_ = arr.reduce((a, b) => (a[0] >= b[0] ? a : b));
      let v = arr.shift();
      //console.log(max_,v,arr)
      if (v!=max_){
        arr.push(v)
      }
      else{
        count+=1
        if(v[1]==m){
          break;
        }
      }
    }
      return count;
  }






for(let i = 1;i<=T*2;i+=2){
let [n, m] = line[i].split(" ").map((x) => Number(x));
let arr = line[i+1].split(" ").map((x,idx) => [Number(x),idx]);
//console.log(n,m,arr)
console.log(solution(arr, m))
}




