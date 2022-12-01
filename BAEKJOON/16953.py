from collections import deque

a,b = map(int,input().split())

cnt = 1
q = deque()
q.append([a, cnt])

while q:
    na, cnt = q.popleft()
    if na <= b:
        if na == b:
            print(cnt)
            exit()
        else:
            plus1 = na * 10 + 1
            mult2 = na * 2
            q.append([plus1, cnt + 1])
            q.append([mult2, cnt + 1])
    else:
        continue

print('-1')

