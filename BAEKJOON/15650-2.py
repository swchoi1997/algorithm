n, m = map(int,input().split())
visited = [False] * n
check = []

def dfs(tmp, m, cnt):
    if tmp == m:
        print(' '.join(map(str,check)))
        return
    for i in range(cnt, n):
        if visited[i] == False:
            visited[i] = True
            check.append(i + 1)
            dfs(tmp + 1, m, i)
            visited[i] = False
            check.pop()
dfs(0, m, 0)
