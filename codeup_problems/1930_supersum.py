def solve(k,n):
    if k == 0:
        memo[0][n] = n
        return n
    if memo[k][n] == -1:
        result = 0
        for i in range(1,n+1):
            result += solve(k-1,i)
        memo[k][n] = result
        return result
    else:
        return memo[k][n]
try:
    while 1:
        k, n = map(int,input().split())
        memo=[[-1 for _ in range(n+1)] for _ in range(k+1)]
        print(solve(k,n))
        print(memo)
except:
    exit()

import sys
for line in sys.stdin:
    k, n = map(int,line.split())