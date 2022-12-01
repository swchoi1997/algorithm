import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find_parent(check, k):
    if check[k] != k:
        check[k] = find_parent(check, check[k]) # 루트 노드를 찾음
    return check[k]

def union_find(check, a, b): # union연산을 해줌 즉 서로다른 두 트리를 합쳐주는 연산
    # 중요한건 여기서 들어온 숫자의 루트노드를 찾아서 union해줘야한다는 것이다 그러니까 루트노트에 아랫쪽에 들어올 수 있게
    a = find_parent(check, a)
    b = find_parent(check, b)
    if a < b:
        check[b] = a
    else:
        check[a] = b
    
n,m = map(int,input().rstrip().split())
check = [i for i in range(n + 1)] # 문제 조건 중 초기에 {0}, {1}, ... {n} 이 각각 n + 1개의 집합을 이루고있따
# print(check)
for _ in range(m):
    zo, a, b = map(int ,input().rstrip().split())

    if zo == 0: # union 연산이 들어올때
        union_find(check, a, b)
    else: # find 연산이 들어올 때
        if find_parent(check, a) == find_parent(check, b):
            print('YES')
        else:
            print('NO')
    print(check)

#분리 집합 알고리즘