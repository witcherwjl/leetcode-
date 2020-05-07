# 递归分治 时间O(n2)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) == 1 or len(postorder)==0:
            return True
        root = postorder[-1]
        first_b = -1
        # 判断是否有错误，从第一个大的地方（即右子树开始处）开始判断
        for i in range(len(postorder)):
            if postorder[i]>root:
                first_b = i
                break
        for i in range(i,len(postorder)):
            if postorder[i]<root:
                return False
        # 分治
        return self.verifyPostorder(postorder[0:i]) and \
                self.verifyPostorder(postorder[i:len([postorder])-1])
# 辅助栈，时间O(n)
'''
倒序遍历，起始根设为无穷大，可以视为开头先遍历 无穷大根节点 的左子树
1. 因为倒序，所以先碰到右子树的节点（即第一个比前一个大的数），之后如果有右子树会递增一段。
    在右子树结束位置（即第一个停止递增的位置，同时也是左子树开始的位置），
    开始弹出右子树节点。最后一个弹出的就是根结点，记录根结点root。
2. 右子树弹出完毕，开始遍历左子树，遇到比root大的说明错误；
循环1，2
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack = []
        root = float("+inf")
        for i in range(len(postorder)-1,-1,-1):
            if postorder[i]>root: return False
            while(stack and postorder[i]<stack[-1]):
                root = stack.pop(-1)
            stack.append(postorder[i])
        return True

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''