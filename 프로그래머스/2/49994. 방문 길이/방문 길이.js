
function setLocation(dir,r,c){
    if (dir==="U"){
        return [r-1, c]
    }
    else if(dir=="D"){
        return [r+1, c]
    }
    else if(dir=="L"){
        return [r, c-1]
    }
    else{
        return [r, c+1]
    }
}

function isValid(r,c){
    return (-6<r && r<6 && -6<c && c<6)
}

function solution(dirs) {
    let [r,c] = [0,0]
    const visited = new Set()
    for(let dir of dirs){
        const [nr, nc] = setLocation(dir,r,c)
        if (!isValid(nr, nc)){continue}
        visited.add(`${nr}${nc}${r}${c}`)
        visited.add(`${r}${c}${nr}${nc}`)
        r=nr
        c=nc
    }
    const answer = visited.size/2
    return answer
}