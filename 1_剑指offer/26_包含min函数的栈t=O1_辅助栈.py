class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num = []
        self.minNum = [] # 辅助栈保存

    def push(self, x: int) -> None:
        self.num.append(x)
        if self.minNum == []:
            self.minNum.append(x)
        elif x<=self.minNum[-1]:
            self.minNum.append(x)

    def pop(self) -> None:
        temp = self.num.pop()
        if temp==self.minNum[-1]:
            self.minNum.pop()

    def top(self) -> int:
        if self.num!=[]:
            return self.num[-1]

    def min(self) -> int:
        if self.minNum!=[]:
            return self.minNum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 
提示：
各函数的调用总次数不超过 20000 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''