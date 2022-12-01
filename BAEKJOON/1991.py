import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = dict()
for _ in range(n):
    a, b, c = map(str, input().rstrip().split())
    graph[a] = [b, c]

def preo(n):
    print(n, end = '')
    if graph[n][0] != '.':
        preo(graph[n][0])
    if graph[n][1] != '.':
        preo(graph[n][1])

def ino(n):
    if graph[n][0] != '.':
        ino(graph[n][0])
    print(n, end = '')
    if graph[n][1] != '.':
        ino(graph[n][1])

def posto(n):
    if graph[n][0] != '.':
        posto(graph[n][0])
    if graph[n][1] != '.':
        posto(graph[n][1])
    print(n, end = '')



preo('A')
print()
ino('A')
print()
posto('A')