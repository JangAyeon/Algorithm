function solution(arrows) {
    const directions = [
        [-1, 0],  // 0: 위
        [-1, 1],  // 1: 오른쪽 위
        [0, 1],   // 2: 오른쪽
        [1, 1],   // 3: 오른쪽 아래
        [1, 0],   // 4: 아래
        [1, -1],  // 5: 왼쪽 아래
        [0, -1],  // 6: 왼쪽
        [-1, -1]  // 7: 왼쪽 위
    ];

    // 현재 위치
    let [r, c] = [0, 0];
    const nodes = new Map();  // 방문한 노드
    const routes = new Map(); // 방문한 간선 (양방향 저장)
    let answer = 0;

    // 시작점 방문 처리
    nodes.set(`${r}_${c}`, true);

    for (let dir of arrows) {
        const [dr, dc] = directions[dir];

        // 2단계 이동 (대각선 교차 방지)
        for (let i = 0; i < 2; i++) {
            const [nr, nc] = [r + dr, c + dc];

            const currKey = `${r}_${c}`;
            const nextKey = `${nr}_${nc}`;
            const routeKey = `${currKey}_${nextKey}`;
            const reverseKey = `${nextKey}_${currKey}`;

            const hasNode = nodes.get(nextKey);
            const hasRoute = routes.get(routeKey);

            // 이미 방문한 노드지만, 처음 가는 간선이면 방이 새로 생김
            if (hasNode && !hasRoute) {
                answer += 1;
            }

            // 방문 처리
            nodes.set(nextKey, true);
            routes.set(routeKey, true);
            routes.set(reverseKey, true);

            // 이동
            r = nr;
            c = nc;
        }
    }

    return answer;
}
