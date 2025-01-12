/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  const arr = [0];
  let answer = 0;
  for (let i = 0; i < gain.length; i++) {
    const num = arr[arr.length - 1] + gain[i];
    answer = Math.max(answer, num);
    arr.push(num);
    console.log(arr, answer);
  }
  return answer;
};
