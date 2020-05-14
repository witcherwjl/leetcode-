class Solution:
    def sumNums(self, n: int) -> int:
        self.res = 0 # 保存结果
        def recur(n):
            n>=1 and recur(n-1) # 在此时短路，终止递归
            self.res += n 
            return self.res
        recur(n)
        return self.res
'''

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000
'''