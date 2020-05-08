n = input()
s = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for t in s:
    n = n.replace(t,"*")
print(len(n))
