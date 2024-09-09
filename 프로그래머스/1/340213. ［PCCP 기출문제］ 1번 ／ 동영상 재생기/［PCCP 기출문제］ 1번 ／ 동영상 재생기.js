

function getSeconds(time){
    const [hh, mm] = time.split(":").map(Number)
    return (hh*60+mm)
}

function movePrev(curr){

     return Math.max(0,curr-10)
}

function getTime(seconds){
    const HH = Math.floor(seconds/60)
    const MM = seconds - 60*HH
    const formattedHours = HH.toString().padStart(2, '0');
    const formattedMinutes = MM.toString().padStart(2, '0');

    // 최종적으로 HH:MM 형식으로 반환합니다.
    return `${formattedHours}:${formattedMinutes}`;

}

function moveNext(curr, end_time){
    return Math.min(end_time, curr+10)
}

function checkOpening(curr, op){
    if(op.start<=curr && curr<=op.end){
        return op.end
    }else{
        return curr
    }
    
}

function solution(video_len, pos, op_start, op_end, commands) {

    const total_time = getSeconds(video_len)
    let curr = getSeconds(pos)
    const op={start:getSeconds(op_start), end:getSeconds(op_end)}
    for(let cmd of commands){
        console.log(cmd, curr, getTime(curr))
          curr = checkOpening(curr, op)
        if (cmd=="next"){
           
            curr =moveNext(curr, total_time,op)
        
        }
        
        else{
            curr = movePrev(curr, total_time)
            
        }
         curr = checkOpening(curr, op)
    }
   const answer =  getTime(curr)
    
    return answer;
}

/**
입력값 〉 "30:00", "00:08", "00:00", "00:05", ["prev"]
기댓값 〉 "00:05"

*/