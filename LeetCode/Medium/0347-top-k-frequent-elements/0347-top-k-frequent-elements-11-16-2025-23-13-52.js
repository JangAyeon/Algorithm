/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counter = new Map()
    for(let i of nums){
        const value = (counter.get(i)+1)||1
        counter.set(i, value)
    }
    const rank = [...counter.entries()].sort((a,b)=>b[1]-a[1])
    const answer = rank.slice(0,k).map(item => item[0])

    return answer
};