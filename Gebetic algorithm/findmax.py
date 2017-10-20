
def find_max(L = []):
    max = L[0][0]
    x1 = L[0][1]
    x2 = L[0][2]
    for i in range(len(L)):
        if max < L[i][0]:
            max = L[i][0]
            x1 = L[i][1]
            x2 = L[i][2]

    return max,x1,x2