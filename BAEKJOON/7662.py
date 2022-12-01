import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    h1 = [] 
    h2 = []
    visited = [False] * (n + 1)
    for i in range(n):
        a, b = map(str, input().rstrip().split())
        b = int(b)

        if a == 'I':
            heapq.heappush(h1, (b, i)) # 최소힙 구연
            heapq.heappush(h2, (-b, i)) # 최대힙 구연 
            visited[i] = True
        
        elif a == 'D':
            if b == 1:
                while h2 and not visited[h2[0][1]]:
                    heapq.heappop(h2)
                if h2:
                    x1, x2 = heapq.heappop(h2)
                    visited[x2] = False
            elif b == -1:
                while h1 and not visited[h1[0][1]]:
                    heapq.heappop(h1)
                if h1:
                    x1, x2 = heapq.heappop(h1)
                    visited[x2] = False

    while h1 and not visited[h1[0][1]]:
        heapq.heappop(h1)
    while h2 and not visited[h2[0][1]]:
        heapq.heappop(h2)

    if h1 and h2:
        print(-h2[0][0], h1[0][0])
    else:
        print('EMPTY')