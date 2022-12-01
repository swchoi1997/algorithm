n, m  = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

max_square = 1
for k in range(n):
    for i in range(m):
        for j in range(m - 1, i, -1):

            if graph[k][i] != graph[k][j]:
                if max_square != 1:
                    continue
                max_square = 1
            else:
                length = (j - i) + 1
                if k + length > n:
                    continue
                
                if graph[k + length -1][i] == graph[k][i] and graph[k + length - 1][j] == graph[k][i]:
                    max_square = max(max_square, length * length)
                    break
                    


print(max_square)