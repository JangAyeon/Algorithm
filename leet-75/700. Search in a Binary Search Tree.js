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
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function (root, val) {
  const que = [];
  que.push(root);

  while (que.length) {
    const node = que.shift();
    //console.log(node.val,val)
    if (node.val == val) {
      return node;
    }
    if (node.right) {
      que.push(node.right);
    }
    if (node.left) {
      que.push(node.left);
    }
  }
  return null;
};
