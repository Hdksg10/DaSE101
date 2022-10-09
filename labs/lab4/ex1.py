#十进制到二进制IP地址转换

def D2B(dec):
    decimalNumber = int(dec, 10)
    res = "00000000"
    resPtr = 7
    while decimalNumber >= 2:
        mod = decimalNumber % 2
        decimalNumber = decimalNumber // 2
        res = res[0:resPtr] + f"{mod}" + res[resPtr+1:32]
        resPtr = resPtr - 1
    res = res[0:resPtr] + f"{decimalNumber}" + res[resPtr+1:32]
    return res

address = input()
decs = address.split(".")
bins = map(D2B, decs)
print("".join(bins))