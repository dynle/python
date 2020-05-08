def solve(a,b):
    global li
    li = [i for i in range(a,b+1)]
    for n in range(1,b+1):
        c = n
        for i in range(len(str(n))):
            c += int(str(n)[i])
        if c in li:
            li.remove(c)
        else:
            continue
    return sum(li)
        
a,b = map(int,input().split())
print(solve(a,b))