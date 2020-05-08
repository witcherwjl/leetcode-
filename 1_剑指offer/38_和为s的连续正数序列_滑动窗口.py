class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left = 1
        sum_ = 1
        res  = []
        for right in range(2, target):
            sum_ += right
            if sum_ == target:
                res.append([j for j in range(left,right+1)])
            elif sum_ > target:
                while(sum_>target):
                    sum_ -= left
                    left += 1
                    if sum_==target:
                        res.append([j for j in range(left,right+1)])
        return res

'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''