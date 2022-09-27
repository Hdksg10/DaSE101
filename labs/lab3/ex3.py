string = input()
maxLength = 1
Length = 1
lastChar = string[0]
for i in range(1, len(string), 1):
    if string[i] == lastChar:
        Length += 1
    else:
        Length = 1
        lastChar = string[i]
    if Length > maxLength:
        maxLength = Length
if maxLength != 1:
    print(maxLength)
else:
    print(False)