'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
'''

# 1. 直接使用递归，超出题目要求复杂度
# 动态规划
# 2. 使用递归和备忘录的方法，较慢
class Solution:
	def fib(self, n: int) -> int:
        #递归
        store = {} # 备忘录
        def recursive(n):
            if str(n) not in store:
                if n==0:
                    return 0
                if n==1:
                    return 1
                store[str(n)] = recursive(n-1)+recursive(n-2)
            return store[str(n)]
        return recursive(n)%1000000007

# 3. 利用本道题的特点，将递归代替为循环
# 转移方程：recursive(n-1)+recursive(n-2)-> a,b = b,a+b
class Solution:
    def fib(self, n: int) -> int:
        # 直接循环使用动态规划
        a = 0
        b = 1
        for i in range(n):
            a,b = b,a+b   # 使用
        print(a,b)
        return a%1000000007