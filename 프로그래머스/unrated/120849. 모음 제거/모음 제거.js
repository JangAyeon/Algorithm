function solution(my_string) {
    const v = ["a", "e", "i", "o", "u"]
    const arr = [...my_string]
    const answer=arr.filter((a)=>!v.includes(a))
    
    return answer.join("");
}