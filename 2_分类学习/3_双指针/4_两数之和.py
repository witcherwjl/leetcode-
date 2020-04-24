'''
这个问题的最基本形式是这样:给你一个数组和一个整数证数组中存在两个数的和为
比如输入target,可以保target,请你返回这两个数的索引。
nums = [3,1,3,6], target = 6,
算法应该返回数组
[0,2]
因为3 + 3 = 6。
'''
class Solution:
    """docstring for Solution"""
    def two_sum(self,num,k):
        from collections import Counter
        now = Counter(num)
        a1 = -1
        b1 = -1
        # 利用哈希表，找到是否有符合的数字
        for i in now:
            temp = k-i
            if temp == i and now[i]>1:
                a1 = b1 = i
                break
            elif temp in now and temp != i:
                a1 = i
                b1 = temp
                break

        # 找到数字后寻找其索引然后返回
        res = []
        if a1==b1:
            count = 2
            for i in range(len(num)):
                if num[i]==a1 and count>0:
                    count -= 1
                    res.append(i)
        else:
            count = 2
            for i in range(len(num)):
                if num[i] == a1 and count>0:
                    count -= 1
                    a1 = -1
                    res.append(i)
                if num[i] == b1 and count>0:
                    b1 = -1
                    count -= 1
                    res.append(i)
        return res


a = Solution()
# 输入
# print(a.two_sum([3,1,3,6],9))