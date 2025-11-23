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
 * @return {boolean}
 */
var isValidBST = function(root) {

    function dfs(node){
        if(!node)return true
        const validLeft =  !node.left || node.val>node.left.val
        const validRight = !node.right || node.val<node.right.val
        return dfs(node.left) && dfs(node.right) && validRight && validLeft
    }
    return dfs(root)
    
};