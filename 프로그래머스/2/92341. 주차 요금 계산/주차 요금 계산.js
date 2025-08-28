function getDepartInfo(records){
        const cars= new Map()
    for(let e of records){
        const [time, key, dir] = e.split(" ")
        const [hh, mm] = time.split(":").map(Number)
        const t = hh*60+mm
        const item = cars.get(key)?[...cars.get(key), t]:[t]
        cars.set(key,item)
    }
    // console.log(cars)
    return cars
}


function solution(fees, records) {
    const result = []
    const info= getDepartInfo(records)
    const [defaultTime,defaultCost, chunkTime, chunkCost] = fees
    // console.log(defaultTime,defaultCost, chunkTime, chunkCost)
    const keys = [...info.keys()].sort((a,b)=>a-b)
    for(let k of keys){
        let answer = 0
        let times = info.get(k)
        times = times.length%2?[...times, 23*60+59]:times
        let t = 0
        while(times.length>0){
            let [end, start] = [times.pop(), times.pop()]
            t+=(end-start)
        }
        
        answer = defaultCost
        t-=defaultTime
        if(t>0){
            answer+=Math.ceil(t/chunkTime)*chunkCost
        }
        
        // console.log(k,t, answer)
        result.push(answer)
    }

    return result;
}