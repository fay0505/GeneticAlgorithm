from math import pi
from math import sin
from transform import binary_to_num as fun

def evaluation(m1, m2, a1, b1, a2, b2, P = []):
    eval = []
    L = len(P)

    for i in range(L):
        tmp1 = P[i][0 : m1]    #x1, x2的编码
        tmp2 = P[i][m1 :]

        x1 = fun(a1, b1, m1, tmp1)
        x2 = fun(a2, b2, m2, tmp2)
        num = 21.5 + x1 * sin(4*pi*x1) + x2 * sin(20*pi*x2)
        k = (num, x1, x2)   #记录适应度，以及对应的x1,x2
        eval.append(k)

    return eval



