# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 改进方案
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == q or root==p:
            # 1. q, p 有一个为父节点，那么返回的肯定是第一个被遍历的，即为父节点
            # 2. q, p 没有父节点，那么直接返回即可
            # 综上，直接返回即可
            return root
        else: 
            # 如果p,q中有一个为公共父节点
            # 那么此时a,b肯定有一个为空
            #  所以不为空那个直接返回，即为结果
            a = self.lowestCommonAncestor(root.left, p, q)
            b = self.lowestCommonAncestor(root.right, p, q)
            
            if a and b:
                return root
            if a: return a
            if b: return b
        return None

# 原始方案，不好

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        a = None 
        b = None
        if root == q or root==p: # 其实压根不用考虑之后的事情，至今return即可
            a = root
            b1 = self.lowestCommonAncestor(root.left, p, q)
            b2 = self.lowestCommonAncestor(root.right, p, q)
            if b1: 
                b = b1
            elif b2: 
                b = b2
        else:
            a = self.lowestCommonAncestor(root.left, p, q)
            b = self.lowestCommonAncestor(root.right, p, q)

        if a and b:
            return root
        if a: return a
        if b: return b
        return None



'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''