from random import randint

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

h = seznam(5000, 1000)

print(h)
print('\n')
print(len(h))
print('\n')

k = vycisti(h)

print(k)