function solution(enroll, referral, seller, amount) {
    // k -> enroll: k의 현재 노드, referral: k의 부모 노드 

    const n = enroll.length
    const m = {}
    const parent={}
    for (let idx=0;idx<enroll.length;idx++){
        let name = enroll[idx]
        m[name]=0
        parent[name]=referral[idx]
    }


    for (let idx=0; idx<seller.length;idx++){
        let node = seller[idx]
        let money = amount[idx]*100
        while(node!="-"){

            m[node]+=money-Math.floor(money*0.1)
            //console.log(node, parent,money-Math.floor(money*0.1))
            node = parent[node]
            money=Math.floor(money*0.1)
            if(money<1){break}
            
        }

    }
    let answer = []
    for(let name of enroll){
        answer.push(m[name])
    }




    return answer;
}