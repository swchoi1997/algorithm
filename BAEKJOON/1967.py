import sys
sys.stdin.readline
sys.setrecursionlimit(1000000)
def dfs(tree, start, result):
    for i ,e in tree[start]:
        if result[i] == 0:
            result[i] = result[start] + e
            dfs(tree, i, result)

n = int(input().rstrip())

tree = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int,input().rstrip().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

result1 = [0 for i in range(n + 1)]
dfs(tree, 1, result1)
result1[1] = 0

point = result1.index(max(result1))

result2 = [0 for i in range(n + 1)]
dfs(tree, point, result2)
result2[point] = 0

print(max(result2))