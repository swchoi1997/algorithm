a, b = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

result = []
def dfs(depth):
    if depth == b:
        print(*result)
        return
    for i in range(len(num)):
        result.append(num[i])
        dfs(depth + 1)
        result.pop() # 이부분이 중요함 백트래킹에서 
dfs(0)