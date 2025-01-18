/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  const vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
  const v = [];
  for (let e of s) {
    if (vowels.includes(e)) {
      v.push(e);
    }
  }
  //console.log(v)
  const answer = [...s].map((curr) => {
    if (vowels.includes(curr)) {
      return v.pop();
    } else {
      return curr;
    }
  });
  //console.log(answer.join(""))
  return answer.join("");
};
