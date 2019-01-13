def counting_sort(A,k):
    #suppose all of element of A  value in (0,k)
    m = []
    result = A[:]
    for i in range(k+1):
        m.append(0)
    #print(m)
    for i in A:
        m[i] += 1
    #print(m)
    for i in range(1,len(m)):
        m[i] += m[i-1]
    #print(m)
    for i in A:
        result[m[i]-1] = i
        m[i] -= 1
    return result
'stable:the same element of input have the same index in output'
L = [1,3,4,5,2,5,6,0,5,3,4,5,0,59,3,45,6,100]
print(counting_sort(L,max(L)))
"""
Radix_sort(A,d): #d:数字的位数,从低位开始排序.
 for i =1 to d
  use a stable sort to sort array on digit i.
bucket_sort(A)
n = A.length
let B[0..n-1] be a new array
for i=0 to n-1
    make B[i] empty list
for i =1 to n
    insert A[i] into list B[nA[i]]
for i =0 to n-1
    sort list B[j] with insertion sort
concatenate the list B[0],B[1],...B[n-1] together in order.


"""
