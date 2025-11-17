/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const counter = new Map()
    for(let i of nums){
        const value = (counter.get(i)||0)+1
        counter.set(i, value)
    }
    const rank = [...counter.entries()].sort((a,b)=>-a[1]+b[1]).slice(0,k)
    console.log(rank)
    const answer = rank.map(item => item[0])
    return answer
};