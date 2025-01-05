/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let start = 0;
  let end = height.length - 1;
  let answer = 0;
  while (end > start) {
    const w = end - start;
    let h;
    if (height[start] > height[end]) {
      h = height[end];
      end -= 1;
      //console.log("end 한칸 앞으로", h)
    } else {
      h = height[start];
      start += 1;
      //console.log("start 한칸 앞으로", h)
    }
    // console.log(end,height[end],  start,height[start],  w, h)
    answer = Math.max(answer, w * h);
  }
  return answer;
};
