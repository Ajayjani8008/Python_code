# now we find fibonaci series with intertive method  
def fibonaci_series(n):
    fib_seri=[0,1]
    for i in range(2,n):
        fibonaci=fib_seri[i-1]+fib_seri[i-2]
        fib_seri.append(fibonaci)
    return fib_seri
f=int(input("Enter the number :"))
print(fibonaci_series(f))

