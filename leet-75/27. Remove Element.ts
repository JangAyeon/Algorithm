function removeElement(nums: number[], val: number): number {
  let pivot = nums.indexOf(val);
  // console.log(pivot)
  if (pivot == -1) return nums.length;
  let index = pivot + 1;

  // if(nums.length==1 && nums[0]==val){
  //     nums[0]=val
  //     move+=1
  // }
  while (index < nums.length) {
    if (nums[index] != val) {
      let temp = nums[index];
      nums[index] = val;
      nums[pivot] = temp;
      pivot += 1;
    }
    index += 1;
  }
  // console.log(nums.length-move, pivot)
  return pivot;
}
