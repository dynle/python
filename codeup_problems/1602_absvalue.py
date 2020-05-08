def solve(n):
    if "." in n:
        return abs(float(n))
    else:
        return abs(int(n)) 

n = input()
print(solve(n))
