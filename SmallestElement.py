arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr[k-1])
