/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const sLowered = [...s.toLowerCase().replace(" ","")]
    const str = sLowered.filter(c => (c.charCodeAt()>=97 && c.charCodeAt()<=122))
    const N = str.length
    for(let i=0;i<N/2;i++){
        if(str[i]!=str[N-1-i]){return false}
    }
    return true
};