'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
通过次数18,263提交次数28,589

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 双端队列(慢，空间大)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 双端队列
        from collections import deque
        d = deque([])
        for i in (nums):
            if i%2==0:
                d.append(i)
            else:
                d.appendleft(i)
        return list(d)
# 左右指针（快，空间小）
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 左右指针
        left = 0
        right = len(nums)-1
        while(left<right):
            while(nums[left]%2==1 and left<right):
                left += 1
            while(nums[right]%2 ==0 and left<right):
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums