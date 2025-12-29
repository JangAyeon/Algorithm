/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    // 구하기 | * 지우고 * 옆에 좌측 문자도 제거
    // s를 뒤에서부터 순회 해 stack에 저장(우측을 먼저 파악 가능), 
    // stack에 가장 최근에 저장된 것(가장 우측에 있는 것이) *이고, 현재 좌측이 문자인 경우 문자 저장 X
    const N = s.length
    const stack = []
    for(let i=N-1;i>-1;i--){
        if(stack.length>0 && stack[stack.length-1]=="*" && s[i]!="*"){
            stack.pop()
        }else{
            stack.push(s[i])
        }
        // console.log(stack)
    }
    let answer = ""
    while(stack.length>0){
        answer+=stack.pop()
    }
    return answer
};