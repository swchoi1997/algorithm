import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int ,input().split())
    build = [[] for _ in range(n + 1)]
    buildTime = [0 for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    _time = list(map(int,input().rstrip().split()))

    for _ in range(k):
        a, b = map(int,input().rstrip().split())
        build[a].append(b)
        indegree[b] += 1

    final_bul = int(input())

    def topology_sort():
        q = deque()
        result = []
        cnt = 0
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append((i, cnt))
                buildTime[i] = _time[i - 1]

        while q:
            now, t = q. popleft()
            t += 1
            for i in build[now]:
                buildTime[i] = max(buildTime[i], buildTime[now] + _time[i - 1])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append((i, t))
       
    topology_sort()
    print(buildTime[final_bul])
