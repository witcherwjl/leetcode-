class Solution:
    def permutation(self, s: str) -> List[str]:
        # 使用切片回溯
        self.res = []
        def recur(now, c):
            n = len(now)
            store = []
            if n==1:
                c1 = c+now[0]
                self.res.append(c+now[0])
                return
            for i in range(n):
                if now[i] not in store:
                    # 使用切片回溯
                    c += now[i]
                    store.append(now[i])
                    recur(now[:i]+now[i+1:],c)
                    c = c[:-1]
        recur(s,"")
        return self.res

class Solution:
    def permutation(self, s: str) -> List[str]:
        # 使用索引递归和交换剪枝
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set() # 用于保存用过的值，剪枝
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res
'''
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
限制：
1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''