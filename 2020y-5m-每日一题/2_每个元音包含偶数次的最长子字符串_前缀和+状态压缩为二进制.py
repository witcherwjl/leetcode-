# 核心思想，利用 00000 五位二进制表示5个字符的奇偶性
# 二进制相同，则两者之间的字符串，5个字符数必定为偶数
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 初始化 index 11111 - 00000的数组
        # 利用ans数组，保存二进制出现的第一个index
        # 当相同二进制出现时，直接计算两者index差，即为子字符长度。

        ans = [-1 for i in range(1<<5)] 
        ans[0] =  0 # 关键步骤，在没有开始前 00000 状态默认在 s[0] 位置
        status = 0 # 用于保存当前各个字符奇偶性
        res = 0 # 计算长度
        for i in range(len(s)):
            if s[i] == 'a':
                status ^= 1<<0
            elif s[i] == 'e':
                status ^= 1<<1
            elif s[i] == 'i':
                status ^= 1<<2
            elif s[i] == 'o':
                status ^= 1<<3
            elif s[i] == 'u':
                status ^= 1<<4

            if ans[status] == -1: # 如果没有过，则将第一次出现的index记录下来
            # 如果字符串中没有元音字母，比如 "mmm"，status保持 0 不变，
            # 用 i + 1 答案是 3， 用 i 的话答案是 2 就不对了
            # 所以上下都用i+1，保持一致
                ans[status] = i+1
            else:
                res = max(res, i+1 - ans[status])
        return res
'''

给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。
'''