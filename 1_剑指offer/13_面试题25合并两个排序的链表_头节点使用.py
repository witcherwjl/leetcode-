'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res =now= ListNode()
        while(l1!=None and l2!=None):
            if l1.val < l2.val:
                now.next = l1
                l1 = l1.next
                now = now.next
            elif l1.val==l2.val:
                now.next =l1
                l1 = l1.next
                now= now.next
                now.next =l2
                l2 =l2.next
                now = now.next
            else:
                now.next = l2
                l2 = l2.next
                now = now.next
        if l1:
            now.next = l1
        else:
            now.next = l2
        return res.next