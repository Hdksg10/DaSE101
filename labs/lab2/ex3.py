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