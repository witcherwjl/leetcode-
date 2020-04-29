'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 1. DFS,深度遍历，需要使用回溯+递归+备忘录保存，需要遍历四个方位
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = [] # 将遍历过的地方保存，做剪枝处理
        def DFS(y,x):
            if (y,x) in res or y<0 or y>=m or x<0 or x>=n:
                return
            # 计算数位之和
            max_k = 0
            temp_y = y
            temp_x = x
            while(temp_y!=0 or temp_x!=0):
                max_k += temp_x%10+temp_y%10
                temp_x //= 10
                temp_y //=10

            if max_k>k:
                dfs(x-1,y)
                dfs(x,y-1)
                return 
            else:
                res.append((y,x))
                dfs(y,x+1)
                dfs(y+1,x)
                dfs(y-1,x)
                dfs(y,x-1)
       	dfs(0,0)
        return len(res)

# 2. BFS，广度遍历，需要使用队列+备忘录，只需要遍历+1位置（向右，向下）即可
# 计算数位之和
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        #BFS
        from queue import Queue
        q = Queue() #队列，保存广度遍历节点
        q.put((0, 0))
        s = set() # 备忘录
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n \
            				and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]: # 遍历两个方位
                    q.put((nx, ny))
        return len(s)