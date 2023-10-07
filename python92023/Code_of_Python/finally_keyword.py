def try_except():
    try:
        l=[1,3,4,56,7,8,5]
        i=int(input("Enter the integer number"))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("i am something") #   compulsory executed
x=try_except()
print(x)

# 37