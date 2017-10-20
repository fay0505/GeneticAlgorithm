
import random

def Initial(m, n):  #n是染色体个数

    P = []
    for i in range(n):
        v = [random.randint(0,1) for j in range(m)]
        P.append(v)

    return P

