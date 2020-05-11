h, m = map(int,input().split())
if m >= 30:
    m -= 30
elif h >= 1:
    h -= 1
    m = 60 - (30-m)
else:
    h = 23
    m = 60 - (30-m)
print("%d %d"%(h,m))