import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
graph = [(list(map(int,input().rstrip().split()))) for _ in range(n)]

def dq(x, y, n):
    if n == 2:
        check = []
        for i in range(x, x + 2):   
           for j in range(y, y + 2):
                check.append(graph[i][j])
        check.sort()
        return check[2]

    else:
        check = []
        for a in range(2):
            for b in range(2):
                check.append(dq(x + n // 2 * a, y + n // 2 * b, n // 2))
        check.sort()
    return check[2]


print(dq(0,0, n))
  


# new_graph = [[0] * (n // 2) for _ in range(n // 2)]

# def dq(x, y, n):
#     if n == 2:
#         check = []
#         for i in range(x, x + 2):
#             for j in range(y, y + 2):
#                 check.append(graph[i][j])
#         check.sort()
#         if x == 0 and y == 0:
#             new_graph[x][y] = check[2]
#         else:
#             new_graph[x//2][y//2] = check[2]

        
#     else:
#         for a in range(2):
#             for b in range(2):
#                 dq(x + n // 2 * a, y + n // 2 * b, n // 2)
    
#     return new_graph

# print(dq(0,0,n))`