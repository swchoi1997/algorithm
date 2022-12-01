import sys
input = sys.stdin.readline

def find_parent(parent, k):
    if parent[k] != k:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]
    

def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x != y:
        parent[y] = parent[x]


n, m = map(int,input().rstrip().split())
parent = [i for i in range(n + 1)]

knowTrue = list(map(int, input().rstrip().split()))[1:]
for i in range(len(knowTrue)):
    union_find(parent, knowTrue[0], knowTrue[i])
# print(parent)
party = []
for _ in range(m):
    party.append(list(map(int, input().rstrip().split()))[1:])

    for i in range(len(party[-1])):
        union_find(parent, party[-1][0], party[-1][i])


    # print(parent)


for i in party:
    for j in range(len(i)):
        if len(knowTrue) > 0 and find_parent(parent, knowTrue[0]) == find_parent(parent, i[j]):
            m -= 1
            break

print(m)

