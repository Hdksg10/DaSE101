Ex1

```python
def fact (x):
    if x != 1:
        return x*(x-1)
    else:
        return x

x = input("Now enter test x:")
print(f"x! is {fact(int(x))}")
```

Ex2

```python
from math import pow

print(pow(27, 1/3))
```

Ex3

```python
coins = [2,2,2,2,2,2,1,2,2,2,2,2,2,2,2]

left = 0
right = len(coins)
mid = (left + right) // 2 
target = -1

while left != mid:
    if mid * 2 != right:
        lsum = sum(coins[left:mid])
        rsum = sum(coins[(mid+1):right])
        if lsum == rsum:
            target = mid
            break
        elif lsum < rsum:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
    else:
        lsum = sum(coins[left:mid])
        rsum = sum(coins[mid:right])
        if lsum == rsum:
            target = mid
            break
        elif lsum < rsum:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2

if target == -1:
    target = left
print(target)
```

Ex4

```python
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
```

