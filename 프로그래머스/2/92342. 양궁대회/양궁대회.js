function solution(n, info) {
  let maxDiff = 0;
  let answer = [-1];

  function dfs(idx, remain, ryan) {
    if (idx === 11) {
      // 남은 화살은 0점 구간에 몰아주기
      if (remain > 0) ryan[10] += remain;

      let apeachScore = 0;
      let ryanScore = 0;
      for (let i = 0; i < 11; i++) {
        if (info[i] === 0 && ryan[i] === 0) continue;
        if (info[i] >= ryan[i]) apeachScore += 10 - i;
        else ryanScore += 10 - i;
      }

      const diff = ryanScore - apeachScore;
      if (diff > 0) {
        if (diff > maxDiff) {
          maxDiff = diff;
          answer = [...ryan];
        } else if (diff === maxDiff) {
          // 낮은 점수 더 많이 맞힌 경우 우선
          for (let i = 10; i >= 0; i--) {
            if (ryan[i] > answer[i]) {
              answer = [...ryan];
              break;
            } else if (ryan[i] < answer[i]) break;
          }
        }
      }

      if (remain > 0) ryan[10] -= remain; // 복구
      return;
    }

    // 현재 점수를 이길 수 있는 만큼 쏘는 경우
    if (remain > info[idx]) {
      ryan[idx] = info[idx] + 1;
      dfs(idx + 1, remain - (info[idx] + 1), ryan);
      ryan[idx] = 0;
    }

    // 현재 점수 포기하는 경우
    dfs(idx + 1, remain, ryan);
  }

  dfs(0, n, Array(11).fill(0));
  return answer;
}
