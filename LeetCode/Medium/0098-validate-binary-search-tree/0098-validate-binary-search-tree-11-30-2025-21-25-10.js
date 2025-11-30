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
    console.log(root.val)
    function isValid(min_, max_, curr, direction){
         // console.log("min_",min_, "max_",max_,"curr",curr,"direction",direction)
        if(curr==null || curr.val==null)return true
        else if(min_>=curr.val || max_<=curr.val){return false}
        else if(curr.left ==null && curr.right ==null){return true}

        return isValid(min_, curr.val ,curr.left,"left") && isValid(curr.val, max_, curr.right,"right")
    }
    const answer = isValid(-Infinity, Infinity, root,"right")
    return answer

}