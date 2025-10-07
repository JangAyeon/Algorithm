function solution(distance, rocks, n) {
    rocks.sort((a, b) => a - b);
    rocks.push(distance);

    let left = 1;
    let right = distance;
    let answer = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        let prev = 0;
        let remove = 0;

        for (let i = 0; i < rocks.length; i++) {
            if (rocks[i] - prev < mid) {
                remove++;
            } else {
                prev = rocks[i];
            }
        }

        if (remove > n) {
            // 너무 많이 제거해야 한다면, 거리 줄이기
            right = mid - 1;
        } else {
            // mid 유지 가능 ⇒ 더 큰 거리 시도
            answer = mid;
            left = mid + 1;
        }
    }

    return answer;
}
