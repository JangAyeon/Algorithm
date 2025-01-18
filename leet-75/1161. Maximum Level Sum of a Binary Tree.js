/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxLevelSum = function (root) {
  const res = [];
  const que = [];
  que.push(root);
  while (que.length > 0) {
    let sum = 0;
    let qLen = que.length;
    while (qLen > 0) {
      qLen -= 1;
      const node = que.shift();
      sum += node.val;
      //console.log(node.val, sum)
      if (node.right) {
        que.push(node.right);
      }
      if (node.left) {
        que.push(node.left);
      }
    }
    res.push(sum);
  }
  const num = Math.max(...res);
  //console.log(res,num)
  return res.indexOf(num) + 1;
};
