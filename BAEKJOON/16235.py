import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

n, m, k = map(int,input().split())

forest = [[5] * n for _ in range(n)]
winterS2D2 = [list(map(int,input().split())) for _ in range(n)]
treecount = 0
tree = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, age = map(int,input().split())
    tree[x -1][y -1].append(age)
    treecount += 1



def springAndSummer():
    global treecount
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue    # 나무가 없으면 바로 continue
            tree[i][j].sort() # 나무를 어린순으로 sort
            tmp_forest = 0 #죽은나무의 양분
            tmp_tree = []
            for k in range(len(tree[i][j])):
                if forest[i][j] >= tree[i][j][k]:
                    forest[i][j] = forest[i][j] - tree[i][j][k]
                    tree[i][j][k] = tree[i][j][k] + 1
                    tmp_tree.append(tree[i][j][k])   
                else:
                    tmp_forest += tree[i][j][k] // 2
                    treecount -= 1
            tree[i][j] = tmp_tree[:]

            #여름
            forest[i][j] += tmp_forest


def fall():
    global treecount
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue    # 나무가 없으면 바로 continue
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for dir in range(8):
                        ni, nj = i + dx[dir], j + dy[dir]
                        if 0 <= ni < n and 0 <= nj < n:
                            tree[ni][nj].append(1)
                            treecount += 1

def winter():
    for i in range(n):
        for j in range(n):
            forest[i][j] += winterS2D2[i][j]
   

for i in range(k):
    springAndSummer()
    fall()
    winter()

print(treecount)
# 5 5 5
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3

# 5 5 5
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3
# 2 1 3
# 3 2 3
# 2 1 3


# 5 2 7
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3

# 10 1 1000
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 100 100 100 100 100 100 100 100 100 100
# 1 1 1