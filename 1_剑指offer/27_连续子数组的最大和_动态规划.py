class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]>0: # 如果是正数说明会增加，此时再+
            	# 直接用nums作为dp数组，保存之前的结果
                nums[i] += nums[i-1] 
        return max(nums)    
'''

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
'''