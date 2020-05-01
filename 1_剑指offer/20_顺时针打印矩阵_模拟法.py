'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        def recur(num):
            m = len(num) # 
            if m==0: return # 防止 []
            n = len(num[0])
            if n==0: return # 防止[[]]
            if m == 1 and n==1:
                res.append(num[0][0]) # 只有一个元素
            elif n==1:
                for i in range(m):
                    res.append(num[i][0])  # 只有一列时
            elif m==1:
                for i in range(n):
                    res.append(num[0][i])  # 只有一行是
            else:
                y,x=0,0
                for i in range(m*2+n*2-4): # 有边界 
                    res.append(num[y][x])
                    if x==0 and y!=0:
                        y -= 1
                    elif y == m-1:
                        x -= 1
                    elif x == n-1:
                        y += 1
                    else:
                        x += 1
                    
            num = num[1:m-1]  # 去掉边界
            for i in range(len(num)):
                num[i] = num[i][1:n-1]
            recur(num) # 递归一下层

        recur(matrix)
        return res