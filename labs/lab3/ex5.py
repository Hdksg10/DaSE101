import random
import math

def f(x):
    return (x * x * x + x * x)

def getInter(right, N = 1000000):
    S = right * 3
    count = 0
    for i in range(N):
        x = random.uniform(0, right)
        y = random.uniform(0, 3)
        if y <= f(x):
            count = count + 1
    return count / N * S

print(getInter(1))