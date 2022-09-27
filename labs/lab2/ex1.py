def fact (x):
    if x != 1:
        return x*(x-1)
    else:
        return x

x = input("Now enter test x:")
print(f"x! is {fact(int(x))}")