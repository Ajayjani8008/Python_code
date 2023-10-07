
# # n = int(input("enter the number n:"))
# # for i in range(1, n+1):
# #     for j in range(1, i+1):
# #         if (i==j):
# #             print("*")
# #     print()
# print("""         * * * * *
#          *       *
#          *       *
#          *       *
#          *       *
#          * * * * *""")


# print("""

#          *
#        * * *
#      * * * * *
#        * * *
#          *    """)


n = int(input("enter the number n:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if ((i == 1) or (i == n)):
            print("*")
           
