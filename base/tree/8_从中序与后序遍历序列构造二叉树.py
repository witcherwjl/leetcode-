'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序和后序，都是先把所有的左子树列出来，所以除了根节点以外，两个列表的左子树数量相同且都在开头
# 先根据后序最后一个找到根节点，然后找到在根中序的位置，确定左右子树的个数，将后序和中序都分割起来再次递归

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == [] or postorder == []:
            return None
        
        # 创建新节点
        now = TreeNode()
        # 提出后序根节点
        now.val = postorder[-1]

        root_in = -1
        for i in range(len(inorder)):
            # 寻找中序根节点
            if inorder[i] == now.val:
                root_in = i
                break

        # 左右子树区间相同，只是顺序不同，所以直接导入递归即可
        now.left = self.buildTree( inorder[:root_in], postorder[:root_in] )
        now.right = self.buildTree( inorder[root_in+1:], postorder[root_in:-1] )
        
        return now
        
