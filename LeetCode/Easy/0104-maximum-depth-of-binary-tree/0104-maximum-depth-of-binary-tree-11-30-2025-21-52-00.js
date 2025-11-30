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
var maxDepth = function(root) {
    function dfs(node, len){
        if(!node){
            // console.log(len)
            return len
        }
        return Math.max(dfs(node.left, len+1), dfs(node.right, len+1))
    }
    return (dfs(root, 0))
    
};