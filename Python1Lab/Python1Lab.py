import random
n=str(input())
p=0
k=list()
for i in range(0,len(n)):
    p=ord(n[i])
    d=round(random.randint(1,100))
    k.append(d)
    print(chr(p+d),end="")
print()
print(*k)
