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
