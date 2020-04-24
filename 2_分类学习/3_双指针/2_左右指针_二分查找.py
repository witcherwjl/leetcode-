def two_sort(num:list, k:int):
    # 有序数组num，寻找k
    left = 0
    right = len(num)-1
    while left<=right:
        mid = (right+left)//2
        if num[mid] == k:
            return mid
        if num[mid] < k:
            left = mid+1
        if num[mid] > k:
            right = mid-1

print(two_sort([2,7,11,24],24))