import math

def iteration(precision = 1e-6):
    init = 1
    step = precision / 10
    while abs((init) * (init) - 2) > precision:
        init = init + step
    return init

def binarySearch(precision = 1e-6):
    min = 0
    max = 2
    mid = (min + max) / 2
    while abs(mid*mid - 2) > precision:
        if mid * mid > 2:
            max = mid
        else:
            min = mid
        mid = (min + max) / 2
    return mid

def newton(precision = 1e-6):
    root = 1
    while abs(root*root - 2) > precision:
        root = (root + 2/root) / 2
    return root

print(newton())