n = int(input())
li = []
li_score = []
for l in range(n):
    v = list(input())
    li.append(v)
    for k in range(len(li)):
        score = 0
        total = 0
        for i in range(len(v)):
            if v[i] == 'O':
                score += 1
                total = total + score
            else:
                score = 0
    li_score.append(total)
for a in range(len(li_score)):
    print(li_score[a])
