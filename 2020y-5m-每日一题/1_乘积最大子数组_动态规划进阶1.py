# 有负数的问题，所以不能直接用 max_n = max(nums[i], max_n*num[i])
# min 保存奇数负数的情况
# max_n 保存连续乘积为正数（全为正数/负数为偶数的情况）的情况，若中断则取最大值

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [-2, 0, 2,  3, -2,   4,   -1]
    #max_n -2, 0, 2,  6, -2,   4,   48
    #min_n -2, 0, 2,  3, -12, -48,  -1
    # res = 48
    
        max_n, min_n, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mi = max_n, min_n
            max_n = max(mx*nums[i], mi*nums[i], nums[i])
            min_n = min(mx*nums[i], mi*nums[i], nums[i])
            res = max(res, max_n)
        return res
'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
