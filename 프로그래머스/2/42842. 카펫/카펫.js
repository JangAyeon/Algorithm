function solution(brown, yellow) {
    let answer = [];
    const n = (brown-4)/2
    for(let x=1;x< 5000 ;x++){
        y = n-x
        // console.log(x,y,x*y)
        if(x*y==yellow){
            answer = [y+2, x+2]
            console.log(x+2, y+2)
            break
        }
    }
    return answer;
}