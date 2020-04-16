'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
# 前序和中序，都是先把所有的左子树列出来，所以除了根节点以外，两个列表的左子树数量相同且都在开头
# 先根据前序第一个找到根节点，然后找到在根中序的位置，
# 确定左右子树的个数，将前序和中序都分割起来再次递归

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == [] or inorder == []:
            return None
        
        now = TreeNode()
        now.val = preorder[0]
        root_in = -1
        
        for i in range(len(inorder)):
            # 寻找根节点，
            if inorder[i] == now.val:
                root_in = i
                break

        # 此处要注意和后序的区别，在给前序时要root的位置+1
        now.left = self.buildTree(preorder[1:root_in+1] , inorder[:root_in],  )
        now.right = self.buildTree( preorder[root_in+1:] ,  inorder[root_in+1:], )
        
        return now
        