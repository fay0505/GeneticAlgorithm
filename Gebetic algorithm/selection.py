import random

def selection( n, e=[], parents = []):
    p = []
    q = []
    L = len(e)
    F = 0

    for i in range(L):
        F += e[i][0]

    for i in range(L):
        p.append(e[i][0] / F)

    for i in range(L):
        tmp = 0
        for j in range(i):
            tmp += e[j][0]
        q.append(tmp)

    r = [random.random() for i in range(n)]   # 产生n组0-1随机数

    newP = []    #新的种群
    for i in range(L):
        if r[i] <= q[i]:
            newP.append(parents[i])
        else:
            for k in range(i+1, L):
                if q[k-1] < r[i] and q[k] >= r[i]:
                    newP.append(parents[k])

    return newP

