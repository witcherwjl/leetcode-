class Solution:
    def translateNum(self, num: int) -> int:
        if num == 0:
            return 1

        n = num
        max_l = 0 # 保存位数
        while(n):
            max_l += 1
            n //=10
        self.res = 0 # 保存数量

        def recur(num,n):
            if n==0:
                return
            if n==1:
                self.res += 1
                return 
            recur(num%pow(10,n-1),n-1) # 去一位
            if num//pow(10,n-2)<26 and num//pow(10,n-2)>9: # 去两位
                if n-2==0: # 如果去掉后没有了，就判断是否符合条件
                    self.res += 1
                recur(num%pow(10,n-2),n-2)

        recur(num,max_l)
        return self.res
'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''