'''
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 暴力运算
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n!=0):
            if n%2 == 1:
                res += 1
            n //= 2
        return res

# &和>>
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n!=0):
            res += n&1 # 判断最后一位是否为1
            n >>= 1 # 循环，每次都右移一位
        return res

# 利用&判断
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n):
            res += 1
            n &= n-1 # 消去n二进制最右边的1，达到减少遍历的效果
        return res