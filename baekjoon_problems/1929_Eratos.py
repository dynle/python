def prime_list(n):
    sieve = [True] * n

    l = int(n ** 0.5)
    for i in range(2, l + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

m,n = map(int,input().split())
li=[]
res = prime_list(n+1)
for i in prime_list(m):
    li.append(i)
for i in li:
    if i in res:
        res.remove(i)
for i in res:
    print(i)
#왜 불가?
# m,n = map(int,input().split())
# for i in prime_list(m):
#     res = prime_list(n).remove(i)
# print(res)
