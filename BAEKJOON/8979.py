import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ranking = [list(map(int,input().split())) for _ in range(n)]
ranking = sorted(ranking, key = lambda x : (-x[1], -x[2], -x[3]))

grade = 1
cnt = 1
for i in range(len(ranking)):
    if i != 0:
        if ranking[i][1:] == ranking[i - 1][1:]:
            cnt += 1
        else:
            grade += cnt
            cnt = 1
                
    if ranking[i][0] == m:
        print(grade)
        exit()