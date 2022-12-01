import sys
input = sys.stdin.readline

n, m = map(int,input().split())
coll = []
for _ in range(n):
    ctnp = list(map(str, input().rstrip().split()))
    coll.append(ctnp)

coll = sorted(coll, key=lambda x : (-int(x[2]), int(x[3])))

check = set()
cnt = 0
while True:
    if coll[cnt][0] in check:
        continue
    else:
        check.add(coll[cnt][0])
        print(coll[cnt][1])
        cnt += 1
    
    if cnt == m:
        break

