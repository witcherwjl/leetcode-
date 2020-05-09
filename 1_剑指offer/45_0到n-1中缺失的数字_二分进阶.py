# 顺序遍历寻找
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]^1
        for i in range(0,len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
# 二分寻找
'''
https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while(i<=j):
            m = (i+j)//2
            if nums[m] == m: i = m+1  # 相同说明缺失在右边
            else: j = m-1   # 若不相同，则说明在左边就有缺失了
        return i 
'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''