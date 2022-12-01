a, b = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
a = []

def dfs(depth, idx):
    if depth == b:
        print(*a)
        return
    for i in range(idx, len(num)):
        a.append(num[i])
        dfs(depth + 1, i)
        a.pop()

dfs(0, 0)



