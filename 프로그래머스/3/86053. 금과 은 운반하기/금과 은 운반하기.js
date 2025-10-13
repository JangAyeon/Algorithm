function solution(a, b, g, s, w, t) {
    let left = 0;
    let right = 1e15; // 충분히 큰 값
    let answer = right;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        let goldSum = 0;
        let silverSum = 0;
        let totalSum = 0;

        for (let i = 0; i < g.length; i++) {
            // mid 시간 동안 왕복 횟수
            let trips = Math.floor(mid / (2 * t[i]));
            if (mid % (2 * t[i]) >= t[i]) {
                trips += 1; // 마지막 편도 가능
            }

            let maxDeliver = trips * w[i];

            goldSum += Math.min(g[i], maxDeliver);
            silverSum += Math.min(s[i], maxDeliver);
            totalSum += Math.min(g[i] + s[i], maxDeliver);
        }

        // 금, 은, 합계 조건 확인
        if (goldSum >= a && silverSum >= b && totalSum >= a + b) {
            answer = mid;       // 가능하면 시간 저장
            right = mid - 1;    // 더 짧은 시간으로 탐색
        } else {
            left = mid + 1;     // 불가능하면 시간 늘림
        }
    }

    return answer; // 최소 시간 반환
}
