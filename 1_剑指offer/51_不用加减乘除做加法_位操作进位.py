class Solution:
    def add(self, a: int, b: int) -> int:
        while(b != 0): # 可能有进位后才能进位的情况
            c = a&b<<1 # 取二进制中有进位的情况，并且向前推一位
            a ^= b # 不考虑进位的和
            b = c # 将进位保存，与不考虑进位相加；可能还有可以进位的情况，所以要循环至无进位情况才可以
        return a
'''
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''