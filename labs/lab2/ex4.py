import random
import math

def f(x):
    return (x * x + 4 * x * math.sin(x))

def getInter(right, N = 1000000):
    S = right * 27
    count = 0
    for i in range(N):
        x = random.uniform(0, right)
        y = random.uniform(0, 27)
        if y <= f(x):
            count = count + 1
    return count / N * S

print(getInter(3) - getInter(2))