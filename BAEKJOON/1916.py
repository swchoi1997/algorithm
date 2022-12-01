import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[]for i in range(n + 1)]
distince = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int,input().rstrip().split())
    city[a].append((b,c))

start,end = map(int,input().rstrip().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distince[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distince[now] < dist:
            continue
        
        for i in city[now]:
            cost = dist + i[1]

            if cost < distince[i[0]]:
                distince[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distince[end])