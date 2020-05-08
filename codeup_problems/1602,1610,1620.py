'''1602'''
def solve(n):
    if "." in n:
        return abs(float(n))
    else:
        return abs(int(n)) 

n = input()
print(solve(n))

'''1610'''
def solve(n,a,b):
    for i in range(b):
        sys.stdout.write(n[a+i])
import sys
n = sys.stdin.readline()
a,b = map(int,sys.stdin.readline().split())
solve(n,a,b)

'''1620'''
def solve(n):
    global total
    total=0
    for i in range(len(n)):
        total +=int(n[i])
    n = total
    if len(str(n)) == 1:
        return print(n)
    else:
        n = str(total)
        solve(n)

n = input()
solve(n)
