'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#利用队列存储每一层的个数
#遍历一层后，将子节点保存入队列中，再循环,直到队列没有元素

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # 1. 若root为空则直接返回,否则定义一个队列，用来储存单层元素
        if root ==None:
            return []
        else:
            queue = [root]

        res = [] # 储存结果

        # 2. 若队列为空，则全部遍历完成
        while(queue != []):

            one = [] # 将每层的元素储存在one中

            # 3.每层节点个数就是queue的长度
            for i in range(len(queue)):
                
                # 4. 出队列。放在now中，将now的子节点加入queue
                now = queue.pop(0)
                one.append(now.val)
                if now.left != None:
                    queue.append(now.left)
                if now.right !=None:
                    queue.append(now.right)

            # 5. 将one结果放入res中
            res.append(one)
        return res
