a = int(input())
b = a
for i in range(1,a+1):
    print(" "*(i-1)+"*"*(2*(b-i)+1))
for k in range(1,b):
    print(" "*(b-k-1)+"*"*(2*k+1))
