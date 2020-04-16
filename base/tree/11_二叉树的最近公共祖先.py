'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归寻找

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def one(now):
            if now == None:
                return now
            
            temp = None # 设置标记，若此节点是 p / q，则记录该值，否则返回None
            
            if now == p or now ==q: #记录
                temp = now
                
            # 遍历所有点
            a = one(now.left) 
            b = one(now.right) 
            
            if a and b: # 两节点共同祖先
                return now
            elif a and temp ==None : # 只找到了一个节点/两个节点有一个为祖先
                return a
            elif b and temp ==None : # temp == None是为了防止两节点有一个为祖先
                return b  			 # 没有temp==None,那么就会跳过返回祖先节点，直接返回
            else:					# 此节点左右子树都没有找到，则返回此节点的标记
                return temp

        return one(root)
