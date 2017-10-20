import random

def crossover(h,m, parents = []):   #h表示给定的交叉概率
    L = len(parents)
    for i in range(0, L, 2):
        r = random.random()
        if r < h:
            cut_point = random.randint(0,m-1)   #随机选出交叉点
            tmp = parents[i][0:cut_point + 1]
            parents[i] = parents[i+1][0 : cut_point+1] + parents[i][cut_point + 1 :]
            parents[i+1] = tmp + parents[i+1][cut_point+1 :]

    return parents

