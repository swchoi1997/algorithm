n,m = map(int,input().split())
check = []

def dfs(tmp, start, cnt):
    if tmp == cnt:
        print(' '.join(map(str, check)))
        return
    for i in range(start, n):
        check.append(i + 1)
        dfs(tmp + 1, i, cnt)
        check.pop()



dfs(0, 0, m)