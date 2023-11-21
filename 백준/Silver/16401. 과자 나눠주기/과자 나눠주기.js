function check(M, snak, ans) {
  let cnt = 0;
  for (let i = 0; i < snak.length; i++) {
    cnt += Math.floor(snak[i] / ans);
  }
  if (cnt >= M)
    return true;
  return false;
}

function binarySearch(M, snak) {
  let answer = 0;

  let left = 1;
  let right = 1000000000;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (check(M, snak, mid)) {
      left = mid + 1;
      answer = mid;
    }
    else {
      right = mid - 1;
    }
  }

  return answer;
}

function sol(M, snak) {
  snak.sort(( a, b ) => a - b);
  console.log(binarySearch(M, snak));
}

function insert() {
  const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
  const [M, N] = input[0].split(' ').map(Number);
  const snak = input[1].split(' ').map(Number);  
  sol(M, snak);
}
insert();