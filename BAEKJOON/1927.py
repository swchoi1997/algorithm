import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())

h = []

for _ in range(int(n)):
    m = int(input().rstrip())

    if m == 0:
        if not h:
            print(0)
            continue
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, int(m))