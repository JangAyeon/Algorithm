/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  let answer = 0;
  for (let i = 0; i < flowerbed.length; i++) {
    const left = i - 1 < 0 ? 0 : flowerbed[i - 1];
    const right = i + 1 >= flowerbed.length ? 0 : flowerbed[i + 1];
    if (flowerbed[i] === 0 && left == 0 && right === 0) {
      answer += 1;
      flowerbed[i] = 1;
    }
  }
  return answer >= n;
};

/**
 *
 * https://www.youtube.com/watch?v=ZGxqqjljpUI
 * padding을 주는 방법 있음
 */
