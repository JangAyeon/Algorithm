function solution(numbers) {
    numbers.sort((a, b) => a - b);
    let count = 0;
    const n = numbers.length;
    for (let i = 0; i < n - 2; i++) {

        for (let j = i + 1; j < n - 1; j++) {

            for (let k = j + 1; k < n; k++) {
                // console.log(i,j,k)
                if (numbers[i] + numbers[j] + numbers[k] == 0) {
                    count++
                    continue
                }
            }
        }


    }
    console.log(count)
    return count
}