/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
  const vowels = ["a", "e", "i", "o", "u"];
  let count = [...s.substring(0, k)].reduce((acc, curr) => {
    if (vowels.includes(curr)) {
      return (acc += 1);
    } else {
      return acc;
    }
  }, 0);
  let maxCount = count;

  for (let i = 0; i + k < s.length; i++) {
    const removed = s[i];
    const added = s[i + k];
    //console.log(removed, added, count)
    if (vowels.includes(removed)) {
      count -= 1;
    }
    if (vowels.includes(added)) {
      count += 1;
    }
    maxCount = Math.max(maxCount, count);
    //console.log(count, s.slice(i, i+k))
  }

  return maxCount;
};
