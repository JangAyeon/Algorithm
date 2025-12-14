var lengthOfLIS = function(nums) {
  const tails = [];

  for (const num of nums) {
    let left = 0;
    let right = tails.length;

    // lower_bound (첫 num 이상 위치)
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (tails[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    tails[left] = num;
  }

  return tails.length;
};
