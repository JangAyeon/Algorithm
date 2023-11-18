const filePath = process.platform==="linux"?"/dev/stdin":"../input.txt"
const fs = require("fs")
const input = fs.readFileSync(filePath).toString().split("\n")

const n = Number(input[0])
const arr = input[1].split(" ")
const nLength = n+1
let nums=Array(10).fill(0).map((_,idx)=>idx)
let answer=[]

function isAble(nums){
  let flag = true
  for(let i=1;i<=nums.length-1;i++){
    // 숫자 2개와 부등호 가져와서 대소 비교 오류없는지
    let prev=nums[i-1]
    let post = nums[i]
    let cmd=arr[i-1]
    if(cmd=="<" &&(prev>post)){
      return false
    }
    else if(cmd==">"&&(prev<post)){
return false
    }
  }

  return true

}


// nums에서 n개 숫자 뽑기
function dfs(depth,result){
  if(depth==n+1){
    if (isAble(result)) {
      // 숫자배열 => 문자열 => 숫자
      answer.push(Number(result.join("")));
    }
    return
  }
  for (let i = 0; i < nums.length; i++) {
    if (!result.includes(nums[i])) {
      result.push(nums[i]);
      dfs(depth + 1, result);
      result.pop();
    }
  }

}

dfs(0,[])
// 최대값 최소값 구하기
let max_ = Math.max(...answer)
let min_ = Math.min(...answer)

// 문자열의 padStart 이용해 자릿수 맞춰서 답
console.log(max_.toString().padStart(nLength, 0));
console.log(min_.toString().padStart(nLength, 0));


