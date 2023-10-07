# x=5
# print(x)
# def hello():
#     x=6
#     print(f"the local x is {x}")
# hello()
# print(f"the global x is {x}")



# let i introduce to global keyword
x=10
def global_keyword():
    global x
    x="jay swaminarayan"
    print(f"the local x is {x}")
global_keyword()
print(f" the changed value of x by globally ...{x}")