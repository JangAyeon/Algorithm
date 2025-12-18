/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let curr = head // 1
    let prev = null
    while(curr!=null){
        // console.log(prev,curr.val)
        const temp = curr.next
        curr.next = prev
        prev = curr
        curr =  temp
    }
 
 // console.log(prev)
 return prev

};