# 添加，暴力排序寻找中位
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.List = []
        self.nums = 0

    def addNum(self, num: int) -> None:
        self.List.append(num)

    def findMedian(self) -> float:
        self.List.sort()
        n = len(self.List)
        print(n)
        if n%2==0:
            return (self.List[n//2]+self.List[n//2-1])/2
        else:
            return self.List[n//2]

# 大小堆，将数字分开保存
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # python 中小顶堆使用的多
        self.left_max_t = [] # 将数字转为负数保存为小顶堆。绝对值大的在根节点，类似于大顶堆
        self.right_min_t = [] # 正常保存为小顶堆，right长度大

    def addNum(self, num: int) -> None:
        # 相同长度，则将num其放入right中比较
        #  将right最小值放入left中，作为left中的最大值
        if len(self.left_max_t) == len(self.right_min_t): 
            heappush(self.right_min_t, num)
            heappush(self.left_max_t, -heappop(self.right_min_t))
        # 不同长度，将 -num 放入left做比较
        # 将left中最大值提出来放入right
        else:
            heappush(self.left_max_t, -num)
            heappush(self.right_min_t, -heappop(self.left_max_t))
        print(len(self.left_max_t),len(self.right_min_t))
        
    def findMedian(self) -> float:
        if len(self.left_max_t)==len(self.right_min_t):
            return ( -self.left_max_t[0]+self.right_min_t[0])/2
        else:
            return -self.left_max_t[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()