def hanoi(num,a,b,c):
    if num == 1:
        res.append((a,c))
        return
    else:
        hanoi(num-1,a,c,b)
        res.append((a,c))
        hanoi(num-1,b,a,c)

N = int(input())
res = []
hanoi(N,1,2,3)
print(len(res))
for i, j in res:
    print(i, j)
