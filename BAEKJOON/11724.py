def find_parent(check, x):
    if check[x] != x:
        return find_parent(check, check[x])
    return x

def union_parent(check, a , b):
    a = find_parent(check, a)
    b = find_parent(check, b)
    if a < b:
        check[b] = a
    else:
        check[a] = b


n, m = map(int, input().split())
check = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().split())

    if find_parent(check, a) == find_parent(check, b):
        continue
    else:
        union_parent(check, a, b)

result = []
for i in check:
    result.append(find_parent(check, i))

result = result[1:]
print(len(set(result)))

#pypy3