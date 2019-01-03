#第二章复习
import random


def merge(left,right):#初始化:new[] is sorted;保持:new[i]<new[i+1];
                    #终止:new 等同于left和right的元素之和.it's we want.
    i,j = 0,0
    new = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1

    if i==len(left):new.extend(right[j:])
    if j==len(right): new.extend(left[i:])
    return new

def merge_sort(L):             #分治法:把原问题分解为规模较小但类似于原问题的子问题,递归的分解原问题变成一系列子问题的集合,
                            #在一个易于求解的规模停止分解,解决子问题,通过子问题于原问题的相似和联系,
                            #合并子问题的解.层层return回归得到原问题的解(有些合并太复杂就...)
    q = len(L)//2
    if len(L)>1:
        left = merge_sort(L[:q])
        right = merge_sort(L[q:])
        L=merge(left,right)
    return L

'''
分析算法
2叉递归树,树高lg(n),一共有lg(n)+1层,每层操作cn次.
T(n)=cnlg(n)+cn=O(nlgn)
数学归纳法证明...
层高 T(2**(n+1))=i+1
T(2**(n+1))==(i+1)+1
'''

L=[random.randrange(i)
for i in range(20,50)]

print(L)
print(merge_sort(L))
