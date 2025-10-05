function solution(bridge_length, weight, truck_weights) {
    truck_weights = truck_weights.map(item =>[item, bridge_length])
    let time = 0
    let bridge = []
    let total = 0
    while((truck_weights.length>0 ||bridge.length>0)){
        time+=1
        if(bridge.length>0){
            const [w,t] = bridge[0]
            if(t-1==0){
                bridge.shift()
                total-=w
                // console.log("빼기",bridge, time,total)
            }
           
            bridge=bridge.map(item => [item[0], item[1]-1])
            // console.log("그냥 지나감",bridge, time,total)
            if(truck_weights.length){
                            const [node_w, node_t] = truck_weights[0]
            if(total+node_w<=weight && bridge_length>=bridge.length){
                truck_weights.shift()
                bridge.push([node_w, node_t])
                total+=node_w
               // console.log("새로 추가",bridge, time,total, truck_weights)
            }
            }

            
        }else{
            const [node_w, node_t] = truck_weights[0]
            truck_weights.shift()
             bridge.push([node_w, node_t])
            total+=node_w
             // console.log("신규 새로 추가",bridge, time,total)
        }
       


        
    }
    var answer = 0;
    
    return time;
}