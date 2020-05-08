def prime_list(n):
    sieve = [True] * n

    l = int(n ** 0.5)
    for i in range(2, l + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

res=[]
for i in range(int(input())):
    n = int(input())
    prime_li=prime_list(n)
    if n >= 4 and n<=10000:
        for l in range(n//2,1,-1):
            if n - l in prime_li:
                j = n - l
                res.append([l,j])
                break
    else:
        exit()
for j in range(len(res)):
    print(res[j][0], res[j][1])
