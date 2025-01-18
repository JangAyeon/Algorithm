/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */

const wordDic = (word) => {
  const dic = new Map();
  for (let w of word) {
    const value = dic.has(w) ? dic.get(w) + 1 : 1;
    dic.set(w, value);
  }
  console.log(dic);
  return dic;
};

const isSameArray = (arr1, arr2) => {
  const n = Math.min(arr1.length, arr2.length);
  for (let i = 0; i < n; i++) {
    if (arr1.pop() !== arr2.pop()) {
      return false;
    }
  }
  return arr1.length > 0 || arr2.length > 0 ? false : true;
};
var closeStrings = function (word1, word2) {
  const word1dic = wordDic(word1);
  const word2dic = wordDic(word2);
  const word1keys = [...word1dic.keys()].sort();
  const word2keys = [...word2dic.keys()].sort();
  const word1values = [...word1dic.values()].sort((a, b) => a - b);
  const word2values = [...word2dic.values()].sort((a, b) => a - b);
  const a = isSameArray(word1keys, word2keys);
  const b = isSameArray(word1values, word2values);
  // console.log(a,b)

  return a && b;
};
