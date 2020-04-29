'''
面试题12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
'''
# 利用BFS（深度）遍历即可，记住回溯用法

# 1. 传递数组
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        m,n = len(board),len(board[0])

        def rective(now,y,x): # 递归
            # 每次符合，都会去掉符合的那个。若数组为空，说明全部符合,则返回True
            if now=="": 
                return True

            for ty,tx in direction:
                temp_y = y+ty
                temp_x = x+tx
                if  temp_x>=0 and temp_x<n and temp_y>=0 and temp_y<m: # 边界条件
                    if board[temp_y][temp_x] == now[0]: # 若符合
                    	# 封掉路径并去掉开头点，进入下一个递归
                        temp, board[temp_y][temp_x] = \
                                    board[temp_y][temp_x], '/' 
                        if rective(now[1:], temp_y, temp_x):
                            return True
                        board[temp_y][temp_x] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: # 寻找和第一个相同的点作为起点
                	# 去掉开头点再递归
                    te, board[i][j] = board[i][j], '/'
                    if rective(word[1:], i, j):
                        return True
                    board[i][j] = te
        
        return False

# 2. 计数
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        m,n = len(board),len(board[0])

        def rective(k,y,x):
            # BFS，回溯
            if board[y][x] == word[k]: # 判断是否相同
                if k+1 ==len(word): return True # 判断是否是最后一个
                temp, board[y][x] = board[y][x], '/' # 替换掉，已经走过的路径禁止通行
                for ty,tx in direction: # 四个方向都走一下
                    temp_y = y+ty
                    temp_x = x+tx
                    if  temp_x>=0 and temp_x<n and temp_y>=0 and temp_y<m:
                            if rective(k+1, temp_y, temp_x): # 如果可以走到底，就返回TRUE
                                return True
                board[y][x] = temp # 将这个路点打开
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if rective(0, i, j):
                    return True
        return False