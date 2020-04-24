def get_1(m,n):
    def dp(i,j):
        # 倒着来
        if i==-1:return i+1
        if j==-1:return j+1
        if m[i]==n[j]:
            return dp(i-1,j-1)
        else:
            return min(
                dp(i,j-1)+1, # 删除n
                dp(i-1,j-1)+1, # 替换
                dp(i-1,j)+1) # 添加n

    return dp(len(m)-1,len(n-1))
