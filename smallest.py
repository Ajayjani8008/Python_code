arr = [25, 11, 7, 75, 5777, 6868, 58588, 78584989, 56]
min = arr[0]
for i in range(0, len(arr)):
    if min > arr[i]:
        min =arr[i]
print(min)
