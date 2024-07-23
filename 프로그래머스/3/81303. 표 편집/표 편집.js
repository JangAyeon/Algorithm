function solution(n, k, cmds) {
    k+=1
    const up = [...new Array(n+2)].map((_,idx)=>idx-1)
    const down = [...new Array(n+2)].map((_,idx)=>idx+1)
    const removed = []
    const answer = new Array(n).fill("O")
    //console.log(k)
    for (const cmd of cmds){
        let [direction, steps] = cmd.split(" ")
        if (direction === "D"){
            while(steps){
            k = down[k]
            steps-=1           
            }
     
        }
        else if (direction === "U"){
                        while(steps){
            k = up[k]
            steps-=1           
            }
        }
        else if (direction=="C"){
            down[up[k]]=down[k]
            up[down[k]]=up[k]
            removed.push(k)
            // console.log(k, n-removed.length)
            k= n<down[k]?up[k]:down[k]
        }
        else{
            restore = removed.pop()
            up[down[restore]]=restore
            down[up[restore]]=restore

            // console.log("restored", restore)
        }
        // console.log(direction, steps,k, removed)
        
    }
    for(let idx of removed){
        answer[idx-1]="X"
    }
    return answer.join("");
}