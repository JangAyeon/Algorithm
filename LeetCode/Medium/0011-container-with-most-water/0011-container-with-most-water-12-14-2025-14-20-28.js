/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {

    let answer = -Infinity
    // let [start, end] = [0, height.lenght-1]
    function getSize(start, end){
        if(start ==end){return}
        const size = Math.min(height[start], height[end])*(end-start)
        answer = Math.max(answer, size)
        if(height[start]<height[end]){
            start+=1
            getSize(start, end)
        }
        else{
            end-=1
            getSize(start, end)
        }
    }
    getSize(0, height.length-1)
    console.log(answer)
    return answer
};