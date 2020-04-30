'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''
# 辅助空间判断是否有重复
class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        res = []
        while(temp!=1):
            now = 0
            while(temp!=0):
                now += (temp%10)**2
                temp //= 10
            temp = now
            if temp in res:
                return False
            else:
                res.append(temp) 
        return True
# 快慢指针，计数判断步数
class Solution:
    def isHappy(self, n: int) -> bool:
        low = n
        fast = n
        count = 0
        while(fast != 1):
            count += 1
            # 快指针，每次都走
            now = 0
            while(fast!=0):
                now += (fast%10)**2
                fast //= 10
            fast = now 
            # 慢指针，两次走一步
            if count %2 ==0:
                now = 0
                while(low!=0):
                    now += (low%10)**2
                    low //= 10
                low = now
            if low == fast:
                return False
        return True
# 递归判断，快慢指针
class Solution:
    def isHappy(self, n: int) -> bool:  
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
