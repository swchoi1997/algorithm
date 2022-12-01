import sys
input = sys.stdin.readline
n = int(input().rstrip())

graph = []
for _ in range(n):
    maps = input().rstrip().split()
    graph.append(maps)

naone, zero, one = 0,0,0

def dq(n, startx, starty):
    global naone, zero, one
    first = graph[startx][starty]
    
    for i in range(startx, startx + n):
        for j in range(starty, starty + n):
            if graph[i][j] != first:
                dq(n//3, startx, starty)
                dq(n//3, startx + n//3, starty)
                dq(n//3, startx + n//3*2, starty)
                dq(n//3, startx + n//3*2, starty + n//3)
                dq(n//3, startx, starty + n//3)
                dq(n//3, startx, starty + n//3*2)
                dq(n//3, startx + n//3, starty + n//3*2)
                dq(n//3, startx + n//3, starty + n//3)
                dq(n//3, startx + n//3*2, starty + n//3*2)
                return
                
    if first == '-1':
        naone += 1
        
    elif first == '0':
        zero += 1
        
    elif first == '1':
        one += 1
    
    return

dq(n, 0, 0)
print(naone)
print(zero)
print(one)