/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode(); 
    let s = dummy;

    while (list1 && list2) {
        if (list1.val <= list2.val) {
            s.next = list1;
            list1 = list1.next;
        } else {
            s.next = list2;
            list2 = list2.next;
        }
        s = s.next;
    }
    
    s.next = list1 || list2;

    return dummy.next; // 이거 없어서 틀린 거임!!!
};