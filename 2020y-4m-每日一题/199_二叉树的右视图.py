
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        a = []
        res = [root]
        while(res):
            n = len(res)
            for i in range(n):
                one = res.pop(0)
                if i ==n-1:
                    a.append(one.val)
                if one.left!=None: res.append(one.left)
                if one.right != None: res.append(one.right)
        return a
