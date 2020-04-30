'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 
提示：
2 <= n <= 1000
'''
# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         dp = [0 for _ in range(n+1)]
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 1
#         for i in range(3,n+1):
#             for j in range(i):
#                 dp[i] = max( dp[i], dp[i-j]*j , j*(i-j) )
#         return dp[n]%1000000007
#https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
class Solution :
    def cuttingRope(self, n: int) -> int:
        # 特殊技巧
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        mod = 1e09+7
        while(n>4):
            res*=3
            res %= mod
            n -= 3
        return int(res*n%mod)
