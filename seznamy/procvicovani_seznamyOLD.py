from random import randint
import time
def seznam(n: int, m: int) -> list:
    x=[]
    def vyplnit(t:list):
        for i in range(n):
            t.append(randint(1,m))
        if len(t) != n:vyplnit(t)
        else:return t
    x=vyplnit(x)
    return x

def vycisti(l:list) -> list:
    x=[]
    for i in l:
        if not i in x:
            x.append(i)
    return x
start_time = time.time()
h = seznam(50000, 50000)
print("--- %s seconds ---" % (time.time() - start_time))

k = vycisti(h)

print(k)