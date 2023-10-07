ajay = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 1
print("noramal arryy")
for i in range(0, len(ajay)):
    print(ajay[i])
# rotat arry ....

for i in range(0, n):
    last = ajay[len(ajay)-1]

    for j in range(len(ajay)-1, -1, -1):
        ajay[j] = ajay[j-1]
    ajay[0] = last
print("rotate arry ")
print(ajay)
