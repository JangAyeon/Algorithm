/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  const [sub1, sub2] = str1.length < str2.length ? [str1, str2] : [str2, str1]; // [짧은거, 긴거]
  const [minStr, maxStr] = [sub1.length, sub2.length];

  if (sub1 + sub2 != sub2 + sub1) {
    return "";
  }

  function getGCD(x, y) {
    // console.log(x,y)
    if (y == 0) {
      // console.log("end", x)
      return x;
    }
    return getGCD(y, x % y);
  }

  const index = getGCD(minStr, maxStr % minStr);
  const answer = sub1.slice(0, index);
  // console.log(index)
  return answer;
};
