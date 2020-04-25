'''
你现在手里有一份大小为 N x N 的「地图」（网格） grid，上面的每个「区域」（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，
请你找出一个海洋区域，这个海洋区域到离它最近的陆地区域的距离是最大的。
我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。
示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。

示例 2：
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。

提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1
'''
# 利用BFS广度遍历，遍历过的点就设为-1作为剪枝，遍历深度即为所求
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)        
        sark = [(i,j) for i in range(n) for j in range(n) if grid[i][j]==1] # 以1的点为起点
        if len(sark)==n**2 or len(sark)==0:
            return -1
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        step = -1
        while(sark):
            for _ in range(len(sark)):
                one_y,one_x = sark.pop(0)
                # grid[one_y][one_x]==-1
                for _y,_x in direction:
                    temp_y = one_y+_y
                    temp_x = one_x+_x
                    if temp_x>=0 and temp_x<n and temp_y>=0 and temp_y<n and grid[temp_y][temp_x] == 0:
                        sark.append((temp_y,temp_x))
                        grid[temp_y][temp_x] = -1  
            step += 1
        return step



                
                    
