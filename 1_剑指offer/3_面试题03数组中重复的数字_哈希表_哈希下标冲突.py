'''
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

限制：
2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 1。排序，再寻找，时间复杂度高 
# 2。哈希表/集合/数组，额外空间 时间O(n),空间O(n)
# 3。哈希表，原地（利用下标定位）(好方法，记住) 时间O(n),空间O(1)

class Solution: # 3。哈希表，原地（利用下标定位）时间O(n),空间O(1)
    def findRepeatNumber(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):

            while index != value:
                if nums[value] == value: # 如果发生冲突，说明有重复数字，返回结果即可
                    return value
                # 下标定位，利用了哈希冲突，类似与哈希表的建立。将index位置为value的那个换个值
                nums[value], nums[index] = nums[index], nums[value] 
        return -1

class Solution: # 2。哈希表/集合/数组，额外空间O(n)
    def findRepeatNumber(self, nums: List[int]) -> int:
        store = {} #store = set()
        for value in nums:
            if value in store:
                return value
            else:
                store[value] = 0 # store.add(value)
        return -1

