import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int,input().split())
start = int(input())

stage = [[] for i in range(v + 1)]
distince = [INF] *(v + 1)

for _ in range(e):
    u, v, w = map(int,input().rstrip().split())
    stage[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distince[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distince[now] < dist:
            continue
        for i in stage[now]:
            cost = dist + i[1]

            if cost < distince[i[0]]:
                distince[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, len(distince)):
    if distince[i] == INF:
        print('INF')
        continue
    print(distince[i])
    