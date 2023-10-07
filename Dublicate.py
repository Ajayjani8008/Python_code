arr=[1,2,2,3,4,4,5,5,6,7,8,9,0]

print("print dublicat element in givan arry")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
       if arr[i]==arr[j]:
            arr[i]=""

print(arr)