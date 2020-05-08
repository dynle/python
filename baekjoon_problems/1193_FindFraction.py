# import sys
# n = int(sys.stdin.readline())
# num = 1
# i=0
# add=0
# u=[]
# d=[]
# both=[]
# for k in range(10000001):
#     i = i + 1 + add
#     if n <= i:
#         if num%2 == 0:
#             for j in range(num):
#                 u.append(1+j)
#                 d.append(num-j)
#                 both.append([1+j,num-j])
#         else:
#             for j in range(num):
#                 u.append(num-j)
#                 d.append(1+j)
#                 both.append([num-j,1+j])
#         ans = both[n-(i-num)-1]
#         print("%d/%d" %(ans[0],ans[1]))
#         break
#     add+=1
#     num+=1
'''short coding'''
X=int(input())

line=1
while X>line:
    X-=line
    line+=1

if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X

print(a, '/', b, sep='')
