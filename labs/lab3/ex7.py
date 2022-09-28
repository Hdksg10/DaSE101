import time
import random
import datetime
import math

pi = math.pi
def MonteCarlo(precision = 1e-8):
    timest = time.process_time()
    cnt = 0
    acnt = 0
    res = 0 
    while abs(res - pi) > precision:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y <= 1:
            cnt += 1
        acnt += 1
        res = 4*cnt / acnt 
    timeed = time.process_time()
    times = timeed - timest
    print(res)
    return times

def Leibniz(precision = 1e-8):
    """
    \pi / 4 = \sum_{k=0}^\infin \frac{(-1)^k}{2k+1}
    """
    timest = time.process_time()
    res = 0
    cnt = 0
    while abs(4 * res - pi) > precision:
        absterm = 1 / (2*cnt + 1)
        term = absterm
        if cnt % 2 != 0:
            term = -absterm
        res = res + term
        cnt = cnt + 1
    print(4*res)
    timeed = time.process_time()
    times = timeed - timest
    return times

def Chudnovsky(precision = 1e-10):
    '''
    1/\pi = 1/53360sqrt{640320} \sum_{k=0}^\infin (-1)^k\frac{(6k)!}{(k!)^3(3k)!} \times \frac{13591409+545140134k}{640320^3k} 
    '''
    timest = time.process_time()
    res = 0
    cnt = 0
    while res == 0 or abs(53360*math.sqrt(640320)/res - pi) > precision:
        term = pow(-1, cnt)*(math.factorial(6*cnt))*(13591409+545140134*cnt)/(((pow(math.factorial(cnt), 3)*(math.factorial(3*cnt)))*(pow(640320, 3*cnt))))
        res = res + term
        cnt = cnt + 1
    print(53360*math.sqrt(640320)/res)
    timeed = time.process_time()
    times = timeed - timest
    return times

print(MonteCarlo())
print(Leibniz())
print(Chudnovsky())