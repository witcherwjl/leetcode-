'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''
        # 暴力
        for i in range(1,len(numbers)):
            if numbers[i]<numbers[i-1]:
                return numbers[i]
        return numbers[0]
        '''

        # 二分变形
		# 解释：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
        left, right = 0,len(numbers)-1
        while(left < right):
            m = (left+right)//2
            # 只和最后的比较，判断最小值，左右序列
            if numbers[m]>numbers[right]:
                # 如果位于左序列，则说明最小值肯定不在m处，直接left=m+1
                left = m+1
            elif numbers[m]<numbers[right]:
                # 如果位于右序列，最小值可能就m处/小于m处，将right=m
                right = m
            else:
                # 如果有重复元素，则将 right -= 1，去掉一个重复元素
                right -= 1
        return numbers[left]