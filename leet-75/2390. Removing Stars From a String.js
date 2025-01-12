/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function (s) {
  const stack = [];
  for (let str of s) {
    //console.log(str)
    if (str != "*") {
      stack.push(str);
    } else {
      stack.pop();
    }
    //console.log(stack)
  }
  const answer = stack.join("");
  //console.log(answer)
  return answer;
};
