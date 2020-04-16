"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root ==None:
            return False
        
        # 审题，必须要叶子节点作为终点，无左右子树才是叶子节点（根节点无左右子树也是叶子），所以加此判断
        def one(now, num):
            if now.left == None and now.right == None:
                # 叶子
                if num+now.val == sum:
                    return True
                else:
                    return False
            elif now.left == None and now.right != None: # 右边有子树
                return one(now.right, num+now.val)
            elif now.left != None and now.right == None: # 左边有子树
                return one(now.left, num+now.val)
            else: # 都有
                return ( one(now.left, num+now.val) or one(now.right, num+now.val) )
            
        
        return one(root, 0)
