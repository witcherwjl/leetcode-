'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
            self.max_l = 0
    def maxDepth(self, root: TreeNode) -> int:
        # 1. 递归寻找
        def one(now, l):
            if now!=None:
                one(now.left, l+1)
                one(now.right, l+1)
            else:
                # 2. 如果到了最底部则比较最大值
                self.max_l  = max(self.max_l, l)
            
        one(root, 0)
        
        return self.max_l
