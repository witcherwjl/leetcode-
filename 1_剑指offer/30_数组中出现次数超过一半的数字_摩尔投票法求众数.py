'''
摩尔投票法：
票数和： 由于众数出现的次数超过数组长度的一半；若记 众数 的票数为 +1+1 ，非众数 的票数为 -1−1 ，则一定有所有数字的 票数和 > 0>0 。
票数正负抵消： 设数组 nums 中的众数为 xx ，数组长度为 nn 。若 nums 的前 aa 个数字的 票数和 = 0=0 ，则 数组后 (n-a)(n−a) 个数字的 票数和一定仍 >0>0 （即后 (n-a)(n−a) 个数字的 众数仍为 xx ）。

作者：jyd
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for i in range(len(nums)):
            if count==0:
                res = nums[i]
            if nums[i] == res:
                count += 1
            else:
                count -= 1
        return res

# 哈希暴力求
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = {}
        for i in range(n):
            if str(nums[i]) in res:
                res[str(nums[i])] += 1
            else:
                res[str(nums[i])] = 1
            if res[str(nums[i])]>n//2:
                return nums[i]
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''