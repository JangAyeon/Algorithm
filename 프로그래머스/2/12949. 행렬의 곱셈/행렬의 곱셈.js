function solution(arr1, arr2) {
    const i = arr1.length
    const j = arr2.length
    const k = arr2[0].length
    const answer = []
    for (let x=0;x<i;x++){
        const row = []
        for (let y=0;y<k;y++){
            let number = 0
            for (z=0;z<j;z++){
                number+=arr1[x][z]* arr2[z][y]
                
            }
            row.push(number)
        }
        answer.push(row)
    }
    return answer;
}