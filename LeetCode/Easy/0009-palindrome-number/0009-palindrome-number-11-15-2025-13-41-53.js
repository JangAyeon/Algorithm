/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const X = `${x}`
    const N = X.length
    if(x<0){return false}
    for(let i=0;i<(N-1)/2;i++){
        // console.log(i,N-i,  X[i],X[N-1-i] )
        if(X[i]!=X[N-1-i]){return false}
    }
    return true
    
};