'''
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 1. 空集和根无节点的情况
        if root==None or (root.left==None and root.right==None):
            return True
        # 2. 根的子节点一方为空 或 两者不相同的情况
        if root.left ==None or root.right ==None or (root.left.val != root.right.val):
            return False
            
        # 3. 将两边的子树分别前序遍历，一个优先遍历左子树，一个优先遍历右子树。若两者对称，则遍历结果应相同
        res_l = []
        res_r = []
        def one_pro(now):
            if now == None:
                res_l.append(None)
                
                return
            res_l.append(now.val)
            one_pro(now.left)
            one_pro(now.right)
            
        def one_bro(now):
            if now == None:
                res_r.append(None)
                return
            res_r.append(now.val)
            one_bro(now.right)
            one_bro(now.left)
        
        one_pro(root.left)
        one_bro(root.right)
        
        # print(res_l)
        # print(res_r)
        
        if res_r == res_l:
            return True
        else:
            return False
        
        
