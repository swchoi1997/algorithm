n, m = map(int,input().split())
check = []
def dfs(tmp, m):
    if tmp == m:
        print(' '.join(map(str, check)))
        return
    for i in range(n):
        check.append(i + 1)
        dfs(tmp + 1, m)
        check.pop()


dfs(0, m)