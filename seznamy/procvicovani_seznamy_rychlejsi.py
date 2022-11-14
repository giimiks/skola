from random import randint
import time

def seznam(n: int, m: int) -> list:
    x=[]
    for i in range(n):
        x.append(randint(1,m))
    return x

def vycisti(l:list) -> list:
    x=[]
    for i in l:
        if not i in x:
            x.append(i)
    return x

start_time = time.time()

h = seznam(10000, 10000)

print("--- %s seconds ---" % (time.time() - start_time))
print(h)
print('\n')

k = vycisti(h)

print(k)