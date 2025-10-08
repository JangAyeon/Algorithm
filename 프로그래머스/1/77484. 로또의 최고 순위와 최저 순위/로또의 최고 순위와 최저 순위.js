function solution(lottos, win_nums) {
    var answer = [];
    const N = 45
    let [zero_cnt, hit_cnt] = [0,0]
    
    const visited = Array.from({length:N+1}).fill(false)
    for(let lotto of lottos){
        if(lotto==0){
            zero_cnt++
            continue
        }
        visited[lotto]=true
    }
    
    for(let win of win_nums){
        hit_cnt = visited[win]?hit_cnt+1:hit_cnt
    }
     // console.log(hit_cnt, zero_cnt)
    const scoreBoard = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    const score={
        min_hit:hit_cnt,
        max_hit:hit_cnt+zero_cnt
    }
    // console.log({
    //     min_hit:hit_cnt,
    //     max_hit:hit_cnt+zero_cnt
    // })
    return [scoreBoard[score.max_hit], scoreBoard[score.min_hit]];
}