/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  const a = Math.min(word1.length, word2.length);
  word1 = [...word1];
  word2 = [...word2];
  //console.log(a)
  let answer = [];
  for (let idx = 0; idx < a; idx++) {
    answer.push(word1.shift());
    answer.push(word2.shift());
  }
  while (word1.length) {
    answer.push(word1.shift());
  }
  while (word2.length) {
    answer.push(word2.shift());
  }

  //console.log(word1, word2, answer)
  return answer.join("");
};
