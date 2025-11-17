/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const counter = new Map()
    const N = s.length
    let [start, end] = [0,0]
    counter.set("a", 0)
    counter.set("b",0)
    counter.set("c", 0)
    counter.set(s[start],1)
    function getSumAble(){
        const a = counter.get("a")>0&& counter.get("b")>0&&counter.get("c")>0
        const b = counter.get("a")+counter.get("b")+counter.get("c") >=3

        return a&b
    }
    let count = 0
    while(start<N){
        while( !getSumAble()&& end<N-1){
            end+=1
            counter.set(s[end], counter.get(s[end])+1)
            //console.log("##",start, end, counter)

        }

        if( getSumAble()){
            let temp = end
            count+=(N-end)
            // while(temp<N-1){
            //     temp+=1
            //     count+=1
                
            // }
           // console.log("### ",end, count)
        }
        // console.log("#",start, end, counter)
        counter.set(s[start], counter.get(s[start])-1)
        start+=1

    }
    return count
};