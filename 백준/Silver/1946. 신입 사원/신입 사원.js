const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split("\n")



const T = Number(input[0])
let line = 1
function solution(arr){
    let min_=1000001
    let count=0
    for(let i=0;i<arr.length;i++){
        const [x,y] = arr[i]
        if(min_>y){
            min_=y
            count+=1
        }
       
    }
    return count
    
}
for(let t=0;t<T;t++){
    const n = Number(input[line])
    let arr=[]
    for(let i=line+1;i<=line+n;i++){
        arr.push(input[i].split(" ").map(Number))
    }
    line+=n+1
    arr.sort((a,b)=>(a[0]-b[0])) // 서류 점수 낮은 사람이 가장 앞에 있음

    answer = solution(arr)

    console.log(answer)
}

// 다른 지원자의 비해 서류 더 떨어짐 && 면접 더 떨짐 => 탈락
// 내가 뒷 사람보다 서류 점수 낮음이 보장됨 
// 뒷사람보다 면접 등수라도 높아야 함 (숫자가 더 작아야 함)
// [ [ 5, 5 ], [ 4, 1 ], [ 3, 2 ], [ 2, 3 ], [ 1, 4 ] ]