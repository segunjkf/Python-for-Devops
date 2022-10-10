x = range(1, 11)

def gen(n):
    for i in range(n):
        yield i


for i in gen(6):
    print(i)
