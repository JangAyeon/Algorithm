/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const pairs = {"}":"{", "]":"[",")":"("}
    const keys = Object.keys(pairs)
    const stack = []
    const N = s.length
    for(let i=0;i<N;i++){
        const c = s[i]
        if(!keys.includes(c)){
            stack.push(c)
        }else{
            if(stack.length==0){return false}
            else{
                const g = stack.pop()
                if(pairs[c]!=g){return false}
            }
        }
        

    }
    return true
    
};