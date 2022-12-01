n, tae, p = map(int,input().split())
if n == 0:
    print('1')
    exit()

score = list(map(int,input().split()))
score.sort(reverse=True)

score2 = []
TF = False

for i in score:
    if i >= tae:
        score2.append(i)
    elif i < tae:
        if TF == False: 
            score2.append(tae)
            score2.append(i)
            TF = True
        else:
            score2.append(i)

if not TF:
    score2.append(tae)

ranking = [[1, 1]]
cnt1, cnt2 = 1, 0
cnt = 1
TF2 = False
for i in range(1, len(score2)):
    cnt += 1
    if score2[i] < score2[i - 1]:
        cnt1 += 1 + cnt2
        ranking.append([cnt, cnt1])
        cnt2 = 0
    else:
        cnt2 += 1
        ranking.append([cnt, cnt1])
        continue
    
for i in reversed(range(len(score2))):
    if score2[i] == tae:
        if ranking[i][0] > p:
            print('-1')
            exit()
        else:
            print(ranking[i][1])
            exit()


