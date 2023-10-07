def fibo_with_recursive(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return fibo_with_recursive(n-1)+fibo_with_recursive(n-2)
    
n=int(input("Enter the n :")) 
for i in range(n):
    print(f"fibonacci({i})={fibo_with_recursive(i)}")
    