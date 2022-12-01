import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    def bfs(a, b):
        q = deque()
        q.append([a, b])
        while q:
            x, y = q.popleft()
            if abs(x - fest[0]) + abs(y - fest[1]) <= 1000: # 페스티발 장소와 갱신된 현재위치
                print('happy') # 어차피 큐에 들어가면 1000 미만의 거리에 있다는 거니까 현재위치가 갱신되면서 마지막 편의점에서 패스티발까지 거리가 1000 미만일때 happy출력
                return
            for i in range(n):
                if not visited[i]:
                    if abs(x - conv[i][0]) + abs(y - conv[i][1]) <= 1000:
                        q.append([conv[i][0], conv[i][1]])
                        visited[i] = True
        
        print('sad')
        return

    n = int(input())
    home = list(map(int,input().split()))
    conv = [list(map(int,input().split())) for _ in range(n)]
    fest = list(map(int,input().split()))

    visited = [False] * (n) #편의점을 방문하였을 때 방문체크

    bfs(home[0], home[1])

