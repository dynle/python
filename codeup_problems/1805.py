import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    li.append((a,b))
for i in sorted(li):
    sys.stdout.write(str(i[0])+" ")
    sys.stdout.write(str(i[1])+"\n")
