'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def singleNumbers(self, nums):
        ret = 0

        for i in nums:
            ret ^= i

        div = 1
        while div & ret == 0:
            # 找到不同位
            div <<= 1

        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
'''
class Solution:
    def singleNumbers(self, nums):
        ret = 0

        # 先将只有一个的元素全部提出来
        # eg [3,10,3,4]
        # 提出来以后 ret = 4+10
        # 4 二进制: 0b100
        # 10 二进制: 0b1010
        # ret 14 二进制：0b1110
        # 从低位开始看，第一个1为在第二个位置，即在0b10处就已经有不同
        for i in nums:
            ret ^= i

        # 寻找不同位，求异或之后的不同位都是1，找到低位的一个即可。
        # 找到 是1 的位，使用 以1开头的二进制div（eg:1/100/10000/10..） 做&即可，
        # 初始div设为1，求&。
        # 循环：1.找 ，若没有，则左移一位。div=2（0b10）
        # 2. 继续求&，若没有，继续左移，div=4（0b100）
        # 重复2，直到&不为0
        # 4，10不同位，0b10
        div = 1
        while div & ret == 0:
            # 找到不同位
            div <<= 1

        # 将a，b分别用来保存两个数
        # 使用 n&div ，可以将两个数分离开
        # eg：4:0b100 ; 10:0b1010; div:0b10;
        #     4&div = 0b0 = 0
        #     10&div = 0b10 = 2
        #     其他的有重复的不用考虑
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


# nums =  [3,10,3,4]
# a = Solution()
# print('res:',a.singleNumbers(nums))
