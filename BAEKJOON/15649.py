m, n = map(int,input().split())
visited = [False] * m
check = []
def dfs(cnt , n):
    
    if cnt == n:
        print(' '.join(map(str,check)))
        return
    for i in range(len(visited)):
        if visited[i] == False:
            visited[i] = True
            check.append(i + 1)
            dfs(cnt + 1, n)
            visited[i] = False
            check.pop()

dfs(0, n)