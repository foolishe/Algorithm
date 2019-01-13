import random

def partition(A,p,r):
    X = random.randint(p,r)
    A[r],A[X] = A[X],A[r]
    i,j = p,p
    while j < r:
        if A[j] < A[r]:
            A[j],A[i] = A[i],A[j]
            i += 1
        j += 1
    A[i],A[r] = A[r],A[i]
    return i

def Randomized_select(A,p,r,i):
    if i >= len(A):
        raise 'out of the list'
    'i,the min element of A[p,r]'
    if p == r:
        return A[p]
    q = partition(A,p,r)
    print(q,A,A[q])
    if i == q:
        return A[q]
    elif i < q:
        return  Randomized_select(A,p,q-1,i)
    else:
        return Randomized_select(A,q+1,r,i)


l = [2,3,5,2,1,4,6,8,750,4,3]
print(Randomized_select(l,0,len(l)-1,1))
