# 算法导论课后复习,没有时间精力做练习题了...let's go to started!



def insert_sort(L): # args=list
    for j in range(1,len(L)): #初始化,j=1: L[:j] is True (sorted)
        key = L[j]
        i = j - 1
        while L[i] >= key and i >=0: #循环不变量保持子集L[:j] is True,j=(n+1): L[:n+1] is True
            L[i+1] = L[i]          # 循环终止时子集L[0:len(l)] is the answer.
            i -= 1
        L[i+1] = key
    return L



L = [6,4,4,65,3,2,5,4,8,23,45]

print(insert_sort(L))

'''
分析算法:
RAM(random-access machine):计算机模型

输入规模,
已排序情况,
运行时间: 执行的基本操作数/指令数/步数(执行每行代码的操作数)

                                    cost         times
for j in range(1,len(L)):           c1           n
    key = L[j]                      c2            n-1
    i = j - 1                       c3            n-1
    while L[i] >= key and i >=0:    ...           ...
        L[i+1] = L[i]
        i -= 1
    L[i+1] = key
return L

best case: when L is sorted ecah while loop just 1 cost T(n)=an+b~~O(n)
worst case:when L is sorted by reversed,each while loop line cost:(n+1)n/2~~T(n)=O(n**2)
'''