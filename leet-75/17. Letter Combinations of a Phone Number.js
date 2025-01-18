/**
 * @param {string} digits
 * @return {string[]}
 */

var letterCombinations = function (digits) {
  digits = digits.split("").map(Number);
  const dic = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };
  const answer = [];
  const arr = [];
  for (let i of digits) {
    arr.push(dic[i]);
  }

  function dfs(level, s) {
    //console.log(level, arr[level])
    if (level == arr.length) {
      if (s.length > 0) {
        answer.push(s);
      }
      return;
    }
    for (let e of arr[level]) {
      dfs(level + 1, s + e);
    }
  }

  dfs(0, "");
  return answer;
};
