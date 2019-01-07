# 以前写过,但是还是被边界弄得头晕了,无语,本以为能轻松写出来

import random

def sort_algorithm(A,q,p):
    i = q
    j = i
    key = A[p]
    while j < p:
        if A[j] < key:
            A[j],A[i] = (A[i],A[j])
            i += 1
        j = j+1
    A[p],A[i] = A[i],A[p]
    return i

def sort_a(A,q,p):
    i = q
    j = i+1
    key = A[q]
    while j <= p:
        if A[j] < key:
            A[i+1],A[j] = A[j],A[i+1]
            i = i+1
        j += 1
    A[i],A[q] = A[q],A[i]
    return i

def quick_sort(A,q,p):
    if  p > q:
        i = sort_a(A,q,p)
        quick_sort(A,q,i-1)
        quick_sort(A,i+1,p)


L = list(random.randrange(i) for i in range(50,70))
#L = [4,5,3,2,1,6]
quick_sort(L,0,len(L)-1)
print(L)
