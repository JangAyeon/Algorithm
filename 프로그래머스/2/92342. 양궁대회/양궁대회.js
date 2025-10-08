function calScore(rinfo, ainfo) {
  let rscore = 0;
  let ascore = 0;

  for (let i = 0; i < 11; i++) {
    if (rinfo[i] === 0 && ainfo[i] === 0) continue;
    if (rinfo[i] > ainfo[i]) rscore += 10 - i;
    else ascore += 10 - i;
  }

  return rscore - ascore;
}

function better(info2, info1) {
  const rInfo2 = [...info2].reverse();
  const rInfo1 = [...info1].reverse();

  for (let i = 0; i < 11; i++) {
    if (rInfo2[i] > rInfo1[i]) return true;
    if (rInfo1[i] > rInfo2[i]) return false;
  }
  return false;
}

function search(idx, n, rinfo, ainfo) {
  if (idx === 11 || n === 0) {
    rinfo[10] += n; // 남은 화살은 0점에 몰아줌
    const diff = calScore(rinfo, ainfo);
    const result = [...rinfo];
    rinfo[10] -= n; // 복구
    return [diff, result];
  }

  // ① 안 쏘는 경우
  const [diff1, info1] = search(idx + 1, n, rinfo, ainfo);

  // ② 쏘는 경우
  let bestDiff = diff1;
  let bestInfo = info1;

  if (n > ainfo[idx]) {
    rinfo[idx] = ainfo[idx] + 1;
    const [diff2, info2] = search(idx + 1, n - rinfo[idx], rinfo, ainfo);
    rinfo[idx] = 0; // 복구

    if (diff2 > bestDiff || (diff2 === bestDiff && better(info2, bestInfo))) {
      bestDiff = diff2;
      bestInfo = info2;
    }
  }

  return [bestDiff, bestInfo];
}

function solution(n, info) {
  const [diff, answer] = search(0, n, Array(11).fill(0), info);
  if (diff <= 0) return [-1];
  return answer;
}
