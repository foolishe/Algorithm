#复习复习.
import random

def Max_heapify(L,i,heap_size):
    '把一个根节点的最大值移动到父节点,如果有交换再对子节点进行递归维护,前提是子节点在开始前都符合heap_tree'
    '这样每次都会有一个节点添加进以子节点为基的heap_tree'
    l = 2*i
    r = 2*i+1
    if l <= heap_size and L[l]>L[i]:
         largest = l
    else:largest = i

    if r <= heap_size and L[r] > L[largest]:
        largest = r
    if largest != i:
        L[i],L[largest] = L[largest],L[i]
        Max_heapify(L,largest,heap_size)


def build_max_heap(L):
    heap_size = len(L)-1
    i = len(L)//2
    while i >= 0:#初始化:L/2 的节点是叶节点(i+1,i+2..len(L)),一个节点的heap
        Max_heapify(L,i,heap_size)#保持:每次i 到 i-1,每次像子节点都是heap树的节点添加一个元素,通过heapify维持.
        i -= 1                    #结束:所有元素都添加进了这颗,L/2的叶节点为基,一个一个扩展了另外L/2的max_heap tree.


def Heap_sort(L):  # '0(nlgn)'
    heap_size = len(L)-1
    build_max_heap(L) #'复杂度 0(n)'
    i = len(L)-1
    while i > 0: #'loop n-1 times'
        L[0],L[i] = (L[i],L[0])
        heap_size -= 1
        Max_heapify(L,0,heap_size) #'lgn'
        i -=1
    return L

L = [random.randrange(i) for i in range(15,33)]
print(L)
print(Heap_sort(L))
