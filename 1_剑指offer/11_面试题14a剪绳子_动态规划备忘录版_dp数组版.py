'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 备忘录版动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        # m>1,n>1
        if n<=2:
            return 1
        store = {}
        def recursive(num):
            if str(num) not in store: # 备忘录
                if num<2:
                    return 1
                max_l = 0
                for i in range(1,num):
                    # 比较2种可能 
                    # 1.(num-i)剪完后大 2.num-i本身大
                    # 1. eg:5,recursive(5)=6>5
                    # 2. eg:3,recursive(3)=2<3
                    max_l =max( max_l,i*recursive(num-i), i*(num-i))
                store[str(num)] = max_l
            return store[str(num)]
        return recursive(n)

# 自底向上，dp数组
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for i in range(n+1)] # 设定dp数组
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1): # 只需要从3开始即可
            for j in range(i):
                # 比较2种可能 
                # 1.(num-i)剪完后大 2.num-i本身大
                # 1. eg:5,recursive(5)=6>5
                # 2. eg:3,recursive(3)=2<3
                dp[i] = max(dp[i],  j * dp[i-j], j*(i-j))
        return dp[n]