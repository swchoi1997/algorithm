import sys
sys.setrecursionlimit(100000)
n = int(input())
set1 = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a = int(input())
    set1[a].append(i)
    # 1234567
    # 3115546
def dfs(start, here, visited):
    # 종료조건!! 
    if visited[here]: # 방문한 곳에 또 방문을 한다면!!
        if start == here: # 그리고 시작과 같다면이라면 사이클이 발생한거임
            return True

    visited[here] = True # 방문 표시를 해주고
    
    nodes = set1[here] # 방문한 곳을 부모노드로 하고 있는 모든 노드를 가져옴
    for i in nodes: # 각 노드들에 대해서 # 3
        if dfs(start, i, visited): #start 를 고정한 후 각 노드들을 탐색했을 때 참이 되는 것이 하나라도 잇으면 그건 사이클이 발생한거임!
            return True 
    return False

result = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if visited[i] == False:
        TF = dfs(i, i, visited)
        if TF == True:
            result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)


