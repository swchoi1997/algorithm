from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n ,m = map(int,input().split())

stage = [(list(map(int,input().rstrip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x, y, z = q .popleft()
        if x == n -1 and y == m -1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if stage[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])
            elif stage[nx][ny] == 1 and z == 0:
                q.append([nx, ny, z + 1])
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
    return -1


print(bfs())




# 1234
# 1115
# 9876
# 10 111
# 11 12 13 14
# 12111
# 13 14 15 16

# 1,0 2,0 3,0 4,0        0000
# 0,2 0,3 0,4 5,5        1110
# 9,3 8,4 7,5 6,6        0000
# 10,4 0,9 0,8 0,7       0111
# 11,5 12,6 13,7 14,8    0000 
# 0,12 0,13 0,14 0,15    
# 0,13 0,14 0,15 0,16    

# q ()







# 6 4
# 0100
# 1110
# 0000
# 0000
# 0111
# 0000

# 6 4
# 0000
# 1100
# 0000
# 0000
# 1011
# 0000

# 8 8
# 01000100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 00010100

# 5 10
# 0000011000
# 1101011010
# 0000000010
# 1111111110
# 1111000000


# 5 5
# 01100
# 01000
# 01110
# 01000
# 00010
# 답 9
