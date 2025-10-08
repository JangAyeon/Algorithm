function solution(dirs) {
    const directions={
        "U":[-1,0],
        "D":[1,0],
        "R":[0,1],
        "L":[0,-1]
    }
    const visited = new Map()
    let [r,c] = [0,0]
    
    for(let dir of dirs){
        const [dr,dc] = directions[dir]
        const [nr, nc] = [r+dr, c+dc]
        if(nr<-5 ||nr>5 || nc<-5 || nc>5 ){continue}
        const [route,reversed] = [`${r}_${c}_${nr}_${nc}`,`${nr}_${nc}_${r}_${c}`]
        visited.set(route,true)
        visited.set(reversed, true)
        r = nr
        c = nc
    }
    
    const answer = visited.size/2
    // console.log(visited, answer)
    return answer;
}