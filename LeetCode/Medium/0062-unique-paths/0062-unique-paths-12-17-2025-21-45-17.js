/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const dp = Array.from({length:m}).fill(0).map(()=>Array.from({length:n}).fill(1))
    for(let r=1;r<m;r++){
        for(let c=1;c<n;c++){
            dp[r][c]=dp[r-1][c]+dp[r][c-1]
        }
    }
    return (dp[m-1][n-1])
    
};