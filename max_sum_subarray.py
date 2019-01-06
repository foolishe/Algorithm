#寻找最大和的连续字数组
import random

def FIND_Maximum_cross_mid_Subarray(A,low,mid,high):
    left_sum = -10**9
    sum = 0
    i = mid
    while i >= 0:
        sum += A[i]
        if sum > left_sum:
            left_low = i
            left_sum = sum
        i-=1

    right_sum = -10*9
    sum=0
    i=mid+1
    while i <= high:
        sum += A[i]
        if sum >= right_sum:
            right_sum = sum
            right_high = i
        i+=1
    print(mid,left_sum+right_sum)
    return left_low,right_high,left_sum+right_sum




def FIND_Maximum_Subarray(A,low,high):
    if high == low:
        return(low,high,A[low])
    else:
        mid = (high+low)//2
        left_low,left_high,left_sum = \
        FIND_Maximum_Subarray(A,low,mid,)
        right_low,right_high,right_sum = \
        FIND_Maximum_Subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum = \
        FIND_Maximum_cross_mid_Subarray(A,low,mid,high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low,left_high,left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low,right_high,right_sum
    else:
        return cross_low,cross_high,cross_sum

def Find_maximum_subarray_liner(L):
    max_subarray_sum = -10**9

    for i in range(len(L)): #循环不变式 i =0, true.保持:i+1,it True.
        sum = 0             #END: subset L[0,len(L)] will be true,and it we want.
        j=i
        while j >= 0:
            sum = sum + L[j]
            if sum > max_subarray_sum:
                max_subarray_sum = sum
                low = j
                high = i
            j-=1
    return low,high,max_subarray_sum


L = (2,5,-5,-3,6,8)
L1=[]
A = (random.randrange(i)*(-1)**i for i in range(10,20))
for i in A:
    L1.append(i)

print(FIND_Maximum_Subarray(L,0,len(L)-1))
print(Find_maximum_subarray_liner(L))
print(L1,'\n',FIND_Maximum_Subarray(L1,0,len(L1)-1))
