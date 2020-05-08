T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    ppl = [i for i in range(1,n+1)] #한줄로 i값을 리스트로 넣기
    for j in range(k):
        for l in range(1,n):
            ppl[l] += ppl[l-1] #값을 저장해서 올라가기
    print(ppl[-1])
