'计算编码的比特位数'
from math import log

def required_bits(p, a1, b1, a2, b2):
    m1 = int(log((b1 - a1)*10**p + 1  , 2) + 1)
    m2 = int(log((b2 - a2)*10**p + 1 , 2) + 1)
    #print('m1:',m1,'m2:',m2)
    return m1 , m2





