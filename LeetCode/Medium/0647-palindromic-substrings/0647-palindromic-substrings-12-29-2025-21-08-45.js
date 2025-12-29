/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    const n = s.length

    function doublepoint(t1, t2) {
        let [start, end] = [t1, t2]
        let step = 0
        while (true) {
            if (s[start - step] != s[end + step]) {
                // console.log("## 2-1",start+step, end+step)

                break
            } else {
               
                if (start - step < 0 || end + step >= s.length) {
                    // console.log("## 2-2",start+step, end+step)
                    break
                }
            }
             step++
        }
        //  console.log("@@ 2:: ", t1,t2, " | ", step, start, end, step > 0 || start == end)
        return step


    }

    function onePoint(t) {
        let step = 0
        let count = 0
        let [start, end] = [t - step, t + step]
        while (true) {
            if (s[start - step] != s[end + step]) {
                break
            } else {
            
                if (start - step < 0 || end + step >= s.length) {
                    
                    // console.log("## 1-2", start + step, end + step)
                    break
                }
            }
           step++
        }
        // console.log("@@ 1:: ", t, " | ", step, start, end, step > 0 || start == end)
        return step


    }
    let answer = 0
    for (let idx = 0; idx < s.length; idx++) {
        answer += (onePoint(idx)+doublepoint(idx, idx + 1))

    }
    // console.log(answer)
    return answer
};