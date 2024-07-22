function solution(n, k, cmds) {
    k+=1
     const up = [...new Array(n+2)].map((_,i)=>i-1)
     const down = [...new Array(n+2)].map((_,i)=>i+1)
     // console.log(up, down)
    const stack = []
    
    for(let cmd of cmds){
        const action = cmd[0]
        if (action=="Z"){
            const restore = stack.pop()
            down[up[restore]]=restore
            up[down[restore]]=restore
           
            // console.log(cmd)
        }
        else if (action=="C"){ // 삭제
            stack.push(k)
            down[up[k]]=down[k]
            up[down[k]]=up[k]
             k=n<down[k]?up[k]:down[k]
            //console.log(cmd)
        }
        else{
            let step = parseInt(cmd.split(" ")[1])
            //console.log(action, step)
            if(action=="D"){
                while(step){
                    k = down[k]
                    step-=1
                }
                
            }
            else{
                while(step){
                    k = up[k]
                    step-=1
                }
            }
        }
    }
    //console.log(stack)
    const answer = new Array(n).fill("O")
    for (const i of stack){
        answer[i-1]="X"
    }
     
    return answer.join("")
}