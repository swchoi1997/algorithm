
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(a, result1, graph):
    for i, e in graph[a]:
        if result1[i] == 0:
            result1[i] =  result1[a] + e
            dfs(i, result1, graph)
            

v = int(input().rstrip())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    info = list(map(int,input().rstrip().split()))[:-1]
    # print(info)
    for j in range(1, len(info), 2):        
        graph[info[0]].append((info[j], info[j + 1]))

result1 = [0 for i in range(v + 1)]

dfs(1, result1, graph)
result1[0] = 0 # 자기자신한테 가는건 0

point = result1.index(max(result1))
result2 = [0 for i in range(v + 1)]
dfs(point, result2, graph)
result2[point] = 0

print(max(result2))

# # ############################# 플로이드 워셜 메모리초과 ###########################3
# import sys
# INF = int(1e9)
# input = sys.stdin.readline

# v = int(input().rstrip())

# graph = [[INF] * (v) for _ in range(v)]
# for i in range(len(graph)):
#     for j in range(len(graph[i])):
#         if i == j:
#             graph[i][j] = 0

# for i in range(v):
#     info = list(map(int,input().rstrip().split()))[1:]
#     for j in range(0, len(info), 2):        
        
#         if info[j] == -1:
#             break
#         else:
#             graph[i][info[j] - 1] = info[j + 1]

# # for i in graph:
# #     print(i)

# for k in range(len(graph)):
#     for a in range(len(graph)):
#         for b in range(len(graph)):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# result1 = 0
# for i in graph:
#     result = max(i)
#     result1 = max(result, result1)
# print(result1)





# 7
# 1 2 1 3 1 -1
# 2 1 1 -1
# 3 1 1 4 3 5 2 -1
# 4 3 3 -1
# 5 3 2 6 3 7 10 -1
# 6 5 3 -1
# 7 5 10 -1
