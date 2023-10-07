def my_generator():
    for i in range(300):
        yield i

gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j+1)


''' ON-THE-FLY(moke par -jb chahiye tab) VALUES GENRET BY Python GENERATER  '''

'''yield show  genereter '''