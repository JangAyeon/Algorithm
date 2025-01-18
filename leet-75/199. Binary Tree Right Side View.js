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
 * @return {number[]}
 */
var rightSideView = function (root) {
  const que = [];
  const res = [];
  que.push(root);
  while (que.length > 0) {
    let rightNode;
    let qLen = que.length;
    while (qLen > 0) {
      const node = que.shift();
      if (node) {
        rightNode = node;
        que.push(node.left);
        que.push(node.right);
      }
      qLen -= 1;
    }
    if (rightNode) {
      res.push(rightNode.val);
    }
  }
  // console.log(res)
  return res;
};
