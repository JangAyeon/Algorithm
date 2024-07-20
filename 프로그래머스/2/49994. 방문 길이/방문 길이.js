


function solution(dirs) {
    const spots = []
    let [r,c] = [0,0]
    const directions = {"U":[-1,0],"D":[1,0],"R":[0,1],"L":[0,-1]}
    for (let dir of dirs){
        let [dr,dc] = (directions[dir])
        let [nr, nc]=[r+dr, c+dc]
   
        if (!((-6<nr && nr<6) && (-6<nc && nc<6))){continue}
        const isExist = spots.some(item => ((item[0]==nr && item[1]==nc && item[2]==r && item[3]==c ) || (item[0]==r && item[1]==c && item[2]==nr && item[3]==nc )  ))
        // console.log([nr, nc], dir,isExist,spots)
        // console.log(isExist, spots,nr, nc)
        if (!isExist){  
              spots.push([r,c,nr, nc])
            spots.push([nr, nc,r,c])        
        }
        

        r=nr
        c= nc
    }
    console.log(spots)
    const answer = (spots,spots.length/2)
    return answer
}