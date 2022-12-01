import sys
input = sys.stdin.readline

def find_parent(check ,k):
    if check[k] != k:
        check[k] = find_parent(check, check[k])
    return check[k]

def union_find(check, a, b):
    a = find_parent(check, a)
    b = find_parent(check, b)

    if a < b:
        check[b] = a
    else:
        check[a] = b

n, m = map(int,input().split())
load = [list(map(int,input().split())) for _ in range(m)]
check = [i for i in range(n + 1)]

load = sorted(load, key= lambda x : (x[2], x[0]))


cnt = 0
for i in range(len(load)):
    if find_parent(check, load[i][0]) == find_parent(check, load[i][1]):
        continue
    else:
        union_find(check, load[i][0], load[i][1])
        cnt += load[i][2]
        last = load[i][2]


print(cnt - last)

# 핵심아이디어는 마지막에 연결되는 간선을 제외하면 두개의 마을로 나뉜다는것이다.
# 그냥 최소 스패닝 트리를 만들다가 마지막에 연결된 간선만 제외하면 어떻게든 두개의 마을로 나뉨!!! 
