let fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().split("\n")

let n = Number(input[0])

function check(arr, count){

  flag = true

  for(let i=0;i<arr.length/2;i++){
  //console.log(i, arr.length-i-1)
  
  let prev = arr[i]
  let post = arr[arr.length-1-i]

  if(prev!=post ){
    if(count==0){
      count+=1
      let arr1 = arr.slice(0, i) + arr.slice(i + 1);
      let arr2 = arr.slice(0, arr.length - i - 1) + arr.slice(arr.length - i);
      flag = Boolean(check(arr1,count)[0]|check(arr2,count)[0])
      //console.log("동시에", flag)
      return [flag,count]

    }
    else{

      flag=false
      break
    }

  }

  }
  //console.log(arr, flag,count)
  return [flag,count]

}

for(let i=1;i<=n;i++){
result = check(input[i], 0);
if(!result[0]){
  console.log(2)
}
else{
  console.log(result[1])
}
}