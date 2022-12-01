import sys
input = sys.stdin.readline

def find_parent(check, k):
    if check[k] != k:
        check[k] = find_parent(check, check[k])
    return check[k]

def union_find(check,a,b):
    a = find_parent(check ,a)
    b = find_parent(check, b)
    if a < b:
        check[b] = a
    else:
        check[a] = b


v, e = map(int,input().split())

tree = []
check = [i for i in range(v + 1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    tree.append([a, b, c])

tree = sorted(tree, key = lambda x : x[2])

cnt = 0
for i in range(len(tree)):
    if find_parent(check, tree[i][0]) == find_parent(check, tree[i][1]):
        continue
    else:
        union_find(check, tree[i][0], tree[i][1])
        cnt += tree[i][2]


print(cnt)
