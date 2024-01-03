function solution(people, limit) {
    let answer = 0;
    people.sort((a,b)=>b-a)
    let h = 0 // 가장 무거운 사람
    let l = people.length-1 // 가장 가벼운 사람
    while(h<=l){
        if(people[h]+people[l]<=limit){ // 보트 탈 수 있음
            l-- // 다음에는 가벼운 사람 태울 거임
        }
        h++
        answer++
    }
    
    return answer;
}