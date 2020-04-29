'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数
判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
'''

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[[]]:
            return False
        for i in range(len(matrix)):
            if target<=matrix[i][-1]: # 如果target大于这行最大的，就不用找了，直接到下一行
                for j in range(len(matrix[0])): # 从最小值开始遍历这一行
                    if target == matrix[i][j]:
                        return True
                    if target<matrix[i][j]: # 由于是升序，若target 比此数还小，直接到下一行
                        break
        return False