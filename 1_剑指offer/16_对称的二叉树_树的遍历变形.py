'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None or (not root.left and not root.right):
            return True
        if not root.left or not root.right:
            return False
            
        # 前序遍历，更换左右顺序即可
        def pro_recur(now):
            if now==None: 
                return '#'
            return str(now.val)+pro_recur(now.left)+pro_recur(now.right)

        def be_recur(now):
            if now==None: 
                return '#'
            return str(now.val)+be_recur(now.right)+be_recur(now.left)

        return pro_recur(root.left) == be_recur(root.right)