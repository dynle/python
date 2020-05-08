n,m = map(int,input().split())
cache=[1]*(n+1)
for i in range(1,n+1):
    cache[i]=cache[i-1]*i
num = cache[n]//(cache[m]*cache[n-m])
v=0
for j in list(str(num))[-1::-1]:
    if j == str(0):
        v+=1
    else:
        break
print(v)