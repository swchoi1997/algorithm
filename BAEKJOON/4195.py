import sys
input = sys.stdin.readline

def find(parent, k):
    if parent[k] != k:
        parent[k] = find(parent, parent[k])
    return parent[k]
    

def union(x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


t = int(input().rstrip())

for _ in range(t):
    f = int(input().rstrip())

    parent = dict()
    number = dict()

    for _ in range(f):
        f1,f2 = input().rstrip().split(" ")

        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1

        union(f1, f2)
        print(number[find(parent, f1)])
    


