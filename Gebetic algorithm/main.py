from representation import required_bits
from initial import Initial
from evaluation import evaluation
from findmax import find_max
from crossover import crossover
from selection import selection
from mutation import  mutation
import pylab as pl
import numpy as np

if __name__ == '__main__':

    str = input("请输入两个变量的区间a1,b1,a2,b2以及保留小数位数p：")
    str_L = str.split(' ')
    a1 = float(str_L[0])
    b1 = float(str_L[1])
    a2 = float(str_L[2])
    b2 = float(str_L[3])
    p = int(str_L[4])

    tmp = required_bits(p,a1,b1,a2,b2)
    m1 = tmp[0]         #计算出需要的比特位数
    m2 = tmp[1]
    m = m1 + m2
    #print('m:',m)

    n =int( input("请输入染色体个数n：") )
    d = int(input("请输入迭代次数d:"))
    h = float(input("请输入交叉概率h:"))
    k = float(input("请输入突变概率k:"))

    ans = []  #记录每一代中适应度最高的值
    Parents = Initial(m, n)

    for i in range(d):
        e = evaluation(m1,m2,a1,b1,a2,b2,Parents)
        max = find_max(e)    #返回的max是一个元组，包含适应度以及对应的x1,x2
        ans.append(max)
        Parents = selection(n,e,Parents)  #选择新一代种群
        Parents = crossover(h,m,Parents)
        Parents =mutation(m,k,Parents)

    result = find_max(ans)
    print('当x1=',result[1],' x2=',result[2],'最大值为：',result[0])
    y = []                        #将每代的适应度放到列表中
    for i in range(len(ans)):
        y.append(ans[i][0])


    x = np.arange(0,d)        #画图
    pl.plot(x,y)
    pl.xlabel('Generation')
    pl.ylabel('z')
    pl.show()

