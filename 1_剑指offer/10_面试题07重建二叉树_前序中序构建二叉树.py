'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder ==[] or inorder==[]:
            return None
        head = TreeNode()
        head.val = preorder[0]
        temp = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                temp = i
        # 分左子树和右子树
        head.left = self.buildTree(preorder[1:temp+1],inorder[0:temp])
        head.right = self.buildTree(preorder[temp+1:],inorder[temp+1:])
        return head