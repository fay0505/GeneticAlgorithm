

def binary_to_num(a, b, m, L = []):
    temp = 1
    num = 0
    for i in range(len(L)):
        num += temp * L[i]
        temp *= 2

    num *= (b - a) / (2**m - 1)

    return a + num