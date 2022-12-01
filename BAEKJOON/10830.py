import sys, copy
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n ,b = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def matrix2(matrix, matrix2):
    tmp_ma = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp_ma[i][j] += matrix[i][k] * matrix2[k][j]
            tmp_ma[i][j] %= 1000
    return tmp_ma


def dq(matrix, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    else:
        tmp = dq(matrix, b // 2)
        if b % 2 == 0:
            return matrix2(tmp, tmp)
        else:
            return matrix2(matrix, matrix2(tmp, tmp))
            

new_matrix = dq(matrix, b)

for i in new_matrix:
    print(*i)
   