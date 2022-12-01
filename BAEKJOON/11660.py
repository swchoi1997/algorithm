import sys
input = sys.stdin.readline

n , m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

graph2 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        graph2[i][j] = graph[i - 1][j - 1] + graph2[i -1][j] + graph2[i][j -1] - graph2[i -1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())

    result = graph2[x2][y2] - graph2[x2][y1 - 1] - graph2[x1 - 1][y2] + graph2[x1 - 1][y1 - 1]

    print(result)










# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().rstrip().split())))

# for _ in range(m): ### O(M)
#     x1, y1, x2, y2 = map(int,input().split())

#     result = 0
#     if x1 == x2:
#         if y1 == y2:
#             print(graph[x1 - 1][y1 - 1])
#             continue
#         else:
#             for i in range(y1 - 1, y2):
#                 result += graph[x1 - 1][i]

#     else:
#         for i in range(x1 - 1 , x2): #O(N)
#             result += sum(graph[i][y1 -1:y2]) #O(N)
#             # O(M * N * N) => O(N^3)

#             # for j in range(y1 - 1, y2):
#             #     result += graph[i][j]


#     print(result)
