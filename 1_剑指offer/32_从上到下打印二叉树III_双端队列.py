# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queqe = []
        queqe.append(root)
        res  = []
        count = 0
        while(queqe):
            t = deque()
            for i in range(len(queqe)):
                temp = queqe.pop(0)
                print(temp.val)
                if count%2==0:
                    t.append(temp.val)
                else:
                    t.appendleft(temp.val)
                if temp.left:
                    queqe.append(temp.left)
                if temp.right:
                    queqe.append(temp.right)
            res.append(list(t))
            count += 1
        return res
'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''