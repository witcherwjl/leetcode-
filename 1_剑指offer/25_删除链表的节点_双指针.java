/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        if(head.next == null)  return head;
        if (head.val == val) return head.next;
        ListNode pro = head.next;
        ListNode re = head;
        while(pro != null && pro.val != val){
            re = pro;
            pro = pro.next;
        }
        if (pro!=null) re.next = pro.next;
        return head;

    }
}