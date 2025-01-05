/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  let p1 = 0;
  let p2 = 0;
  while (p2 < t.length) {
    // console.log(s[p1], t[p2])
    if (s[p1] == t[p2]) {
      p1 += 1;
    }
    p2 += 1;
  }
  const answer = p1 == s.length ? true : false;
  // console.log(p1, answer)
  return answer;
};
