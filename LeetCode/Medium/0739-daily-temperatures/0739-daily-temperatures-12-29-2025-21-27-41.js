/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    // 내 뒤로 가장 빠른 따뜻한 날과 현재 날짜의 차이
    
    // 현재 날짜(index)와 그 뒤로 가장 빨리 따뜻한 날짜 차이 저장하는 배열
    const N = temperatures.length
    const arr = Array.from({length:N}).fill(0)
    const stack = [N-1] // 내 뒤로 나보다 따뜻한 날들 모음
    // 뒤에서부터 시작
    for(let i=N-2;i>-1;i--){
        while(stack.length>0 && temperatures[stack[stack.length-1]]<=temperatures[i]){
            stack.pop()
        }
        if(stack.length>0){
            arr[i] = stack[stack.length-1]-i
        }
        
        stack.push(i)
        console.log(stack,temperatures[i],arr)
    }
    return arr
};