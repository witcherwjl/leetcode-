# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        if head.val == val:
            return head.next
        pro = head.next
        ra = head
        while(pro != None and pro.val != val):
            ra = pro
            pro = pro.next
        if pro != None:
            ra.next = pro.next
        return head