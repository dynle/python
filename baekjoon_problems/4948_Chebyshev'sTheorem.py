all=[]
a = 0
while True:
    n = int(input())
    if n != 0:
        a=1
        li = []
        for j in range(n+1,2*n+1):
            if j == 2:
                li.append(j)
            elif j != 1:
                for k in range(2,j):
                    if j % k == 0:
                        break
                    elif k == j - 1:
                        li.append(j)
            else:
                continue
        all.append(len(li))
    else:
        break
for i in all:
    print(i)
