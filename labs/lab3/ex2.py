

from audioop import reverse


l = [1,2,3,4,5]
for i in range(len(l)-1, -1, -1):
    print(l[i], end=" ")

print("\n")

ct = 1
length = len(l)
while ct <= length:
    print(l[length - ct], end=" ")
    ct = ct + 1
print("\n")

for i in l[-1:-6:-1]:
    print(i, end=" ")
