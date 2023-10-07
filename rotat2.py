arr = []
n = int(input("Enter size of arry   "))
for i in range(0, n):
    arr.append(int(input("enter value of the arry  ")))

for i in range(0, n):
    temp = arr[0]
    for j in range(0, n-1):
        arr[j] = arr[j+1]
    arr[n-1] = temp
    print(arr)
