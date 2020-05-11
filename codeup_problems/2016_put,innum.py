n = int(input())
num = input()
li = list(num)
if len(li) == n:
    for a in range(-3,-n,-3):
        li[a] = ","+li[a]
    for j in li:
        print(j,end="")