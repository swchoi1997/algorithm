import sys, heapq
input = sys.stdin.readline

n = int(input())

h = []
for _ in range(n):
    x = int(input())

    if x == 0:
        print(0) if not h else print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -x)

    