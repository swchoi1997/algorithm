from collections import deque

INF = int(1e9)

f,s,g,u,d = map(int,input().split())

ns = [u, -d]

building = [0 for _ in range(f + 1)]
check = [0 for _ in range(f + 1)]

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        cur = q.popleft()
        for i in range(2):
            next_cur = cur + ns[i]

            if 0 < next_cur <= f and check[next_cur] == 0 and s != next_cur:
                building[next_cur] = building[cur] + 1
                check[next_cur] = 1
                q.append(next_cur)

bfs(s)

if building[g] == 0:
    if g == s:
        print(0)
    else:
        print("use the stairs")
else:
    print(building[g])