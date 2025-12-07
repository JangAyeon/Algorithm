/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const N = prices.length
    const dp = Array.from({length:N}).fill(0)
    const answer = Array.from({length:N}).fill(0)

    for(let i=0;i<N;i++){
        if(i==0){dp[i]=prices[i]}
        else{
            dp[i] = Math.min(dp[i-1],prices[i-1])
        }
        answer[i] = prices[i]-dp[i]
        
    }

    console.log(answer)

    return Math.max(...answer)
   
    
};