function solution(phone_book) {
    var answer = true;
    phone_book.sort()
    // console.log(phone_book)
    for(let idx=0;idx<phone_book.length-1;idx++){
        const a = phone_book[idx]
        const b = phone_book[idx+1].slice(0,phone_book[idx].length)
        // console.log(a,b)
        if(a==b){
            answer = false
            break
        }
    }
    return answer;
}