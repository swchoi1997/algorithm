n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

d = [[0] * (i + 1) for i in range(n)]
d[0][0] = graph[0][0]


for i in range(1, n):
    lilen = len(graph[i])
    for j in range(lilen):
        if j == 0:
            d[i][j] = d[i-1][j] + graph[i][j]
        elif j == len(graph[i])-1:
            d[i][j] = d[i-1][j-1] + graph[i][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + graph[i][j]

print(max(d[n-1]))
