import time
# print(4)
# time.sleep(3)
# print("this is printed after 3 second")
t=time.localtime()
formeted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formeted_time)


d=time.localtime()
formeted_time2=time.strftime("%Yyyy-%myyy-%dyy %H:%M:%S",d)
print(formeted_time2)
