# 暴力求解
# 时间 N^2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        queqe = nums[0:k]
        max_l = max(queqe)
        for i in range(k-1,len(nums)):
            res.append(max(nums[left:right]))
            right += 1
            left += 1
        return res


# 单调栈，保存窗口内最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queqe = []

        # 初始化窗口
        for i in range(0,k):
            while(queqe and nums[i]>queqe[-1]): # 将比此时小的全部踢出
                queqe.pop(-1)
            queqe.append(nums[i])
        res = [queqe[0]]

        # 进行循环
        for i in range(k,len(nums)):
            if nums[i-k] == queqe[0]:
                queqe.pop(0)
            while(queqe and nums[i]>queqe[-1]): # 将比此时小的全部提出，保持双端队列单调性
                queqe.pop(-1)
            queqe.append(nums[i])            
            res.append(queqe[0])           
        return res
        