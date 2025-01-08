/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  const answer = [];
  const max_ = Math.max(...candies);
  for (let i = 0; i < candies.length; i++) {
    const arr = [...candies.slice(0, i), ...candies.slice(i + 1)];
    // console.log(arr, candies[i]+extraCandies, Math.max(...arr))
    if (candies[i] + extraCandies >= max_) {
      answer.push(true);
      //candies[i]+=extraCandies
    } else {
      answer.push(false);
      //candies[i]+=extraCandies
    }
    //console.log(answer)
  }
  return answer;
};
