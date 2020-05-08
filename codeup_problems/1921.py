#Use only 2 and 16. Need to add other numbers
import sys

def solve_2(n):
    if n == 1:
        sys.stdout.write(str(1))
        return
    solve_2(n//2)
    sys.stdout.write(str(n%2))

result=""
def solve_16(n):
    global result
    if n < 16:
        result +=str(n)
        return
    solve_16(n//16)
    result +=str(n%16)

n, k = map(int,sys.stdin.readline().split())
if n == 0:
    sys.stdout.write(str(0))
else:
    if k == 2:
        solve_2(n)
    else:
        solve_16(n)
        new = result.replace("10","A").replace("11","B").replace("12","C").replace("13","D").replace("14","E").replace("15","F")
        sys.stdout.write(new)