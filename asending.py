
arr = [5, 2, 8, 7, 8, 7, 6, 4, 3, 5, 6, 7, 2, 4, 88, 1]
temp = 0


print("Elements of original array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")


for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print()


print("Elements of array sorted in ascending order: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
