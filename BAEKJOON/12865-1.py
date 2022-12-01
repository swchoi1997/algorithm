import sys
input = sys.stdin.readline

n ,k = map(int,input().split())
items = []
for _ in range(n):
    items.append(list(map(int,input().split())))

for i in range(len(items)):
    wei = k
    