function solution(arr)
{
    const stack = [arr[0]]
    const N = arr.length
    for(let i=1;i<N;i++){
        if(stack[stack.length-1]!=arr[i]){
            stack.push(arr[i])
        }
    }
    console.log(stack)
    return stack;
}