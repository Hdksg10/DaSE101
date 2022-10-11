def BubbleSort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] >= arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

lis = [5, 4 ,3, 3, 1]
BubbleSort(lis)
print(lis)