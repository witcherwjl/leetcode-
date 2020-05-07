# 固定一个然后二分查找下一个
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 二分
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < target:
                temp = target-nums[i]
                left = 0
                right = i-1
                while(left<=right):
                    mid = (left+right)//2
                    if nums[mid]==temp:
                        return [nums[mid],nums[i]]
                    elif nums[mid]>temp:
                        right = mid-1
                    else:
                        left = mid+1
        return []
# 双指针移动，和s, target
# s > target
# s = target
# s < target
# 证明 ,利用数字组合图证明
# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while(left<right):
            temp = nums[left]+nums[right]
            if temp == target:
                return [nums[left], nums[right]]
            elif temp>target:
                right -= 1
            else:
                left += 1
        return []