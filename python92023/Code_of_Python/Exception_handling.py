a=input("Enter the number: ")
print(f"The multiplication table of the {a} is :")
try:
    for i in range(1,11):
        print(f"{(a)} X {i}={int(a)*i}")
except Exception as e:
    print(e)
    print("sorry some erroer occurred")
except ValueError:
    print("Enter an integer")
except IndexError:
    print(" index invalid")


