#切割钢条
#length  i(1, 2 ,3..10 )
#price p(i) i = (1,2...,10)
'''
1. 刻画一个最优解的结构特征
r(n) = max(Pn,r1+r(n-1),r2+(n-2),...r(n-1)+r1)
r(n) = max(P(i)+r(n-i)), i =(1,2...n)
2. 递归地定义最优解的值
3. 计算最优解的值,通常采用自底向上的方法
4. 利用计算出的信息构造一个最优解
'''

'钢条价格'
P = [0,1,5,8,9,10,17,17,20,24,30]

def extended_bottom_up_cut_rod(p,n):
    r,s = [],[]
    for i in p:
        r.append(0)
        s.append(0)
    j = 1
    while j <= n:
        q = -1
        i = 1
        while i <= j:
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
            r[j] = q
            i += 1
        j += 1
    return r,s

def print_cut_rod_solution(p,n):
    r,s = extended_bottom_up_cut_rod(p,len(p)-1)
    res = []
    while n > 0:
        res.append(s[n]) # p[i] + max(r[n-i]),max(r[n-i]) = s[n-s[n]]
        n = n - s[n]
    return r,s,res

for i in print_cut_rod_solution(P,7):
    print(i)
