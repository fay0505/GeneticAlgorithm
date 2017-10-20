
import random

def mutation(m,k , parents = []):   # k突变概率
    for i in range(len(parents)):
        r = random.random()
        if r < k:
            point = random.randint(0,m-1)
            if parents[i][point]  == 1:
                parents[i][point] = 0
            else:
                parents[i][point] = 1

    return parents
