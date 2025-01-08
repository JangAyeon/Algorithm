/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  s = s.trim().split(" ").reverse();
  const answer = [];
  for (let e of s) {
    if (e.trim().length > 0) {
      answer.push(e);
    }
  }

  console.log(answer.join(" "));
  return answer.join(" ");
};
