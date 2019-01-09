# 复习.
#每次迭代至少确定一个值A[r]的位置.partition的复杂度为0(n),最多调用partionN次

#随机化A[r],partition的期望比较次数为nlogn

import random,math


count = 0
def partition(A,p,r):
    global count
    x = A[r]
    i = p-1
    j = p
    while j < r:
        if A[j] < x:
            i += 1
            A[i],A[j] = A[j],A[i]
        j += 1
        count += 1
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def quicksort(A,p,r):
    if p < r:
        i = random.randint(p,r)
        A[r],A[i] = A[i],A[r] #随机变换key,经测试work.

        q = partition(A,p,r)
        quicksort(A,p,q-1)
        #p = q+1 尾递归
        quicksort(A,q+1,r)

L = [random.randrange(i) for i in range(10,300)]
quicksort(L,0,len(L)-1)
print(L,'\n  count:',count,' nlgn:',len(L)*math.log2(len(L)))
