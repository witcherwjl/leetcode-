# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 链表结尾不是None，而是链表中某个节点，从而形成了个环
# 寻找环的开头
class Solution:
    def get_huan(self,c:ListNode): # 链表头节点
        low = fast =c
        while(low!=fast):
            # 快慢指针先跑过去，相遇则暂停
            low=low.next
            fast = fast.next.next
        low = c # 将low返回开头
        while(low!=fast):
            # 再匀速进行，再次相遇时肯定会碰在环的开头
            low = low.next
            fast = fast.next

        return low