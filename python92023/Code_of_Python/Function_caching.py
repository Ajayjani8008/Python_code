# import functools
import time
# @functools.lru_cache(maxsize=None)


from functools import lru_cache
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5
print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(7))
print("done for 7")

print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(7))
print("done for 7")

print(fx(20))
print("done for 20")
print(fx(6))
print("done for 6")
print(fx(7))

print("done for 7") 
print(fx(71))
print("done for 71")


''' PLEASE NOTE THAT  IF IS PROGRAM RE-RUN THEN CACHE MEMORY IS CLEAR  AND REGENERATE  FOR NEXT RUN'''


