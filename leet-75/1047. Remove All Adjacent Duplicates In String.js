/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function (s) {
  const stack = [];

  for (let e of s) {
    if (stack.length > 0) {
      if (stack[stack.length - 1] === e) {
        stack.pop();
      } else {
        stack.push(e);
      }
    } else {
      stack.push(e);
    }
    //console.log(stack)
  }
  return stack.join("");
};
