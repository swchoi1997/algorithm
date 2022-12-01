import sys

n, m = map(int, input().split())

name1 = []
for _ in range(n):
    name1.append(sys.stdin.readline().rstrip())

name2 = []
for _ in range(m):
    name2.append(sys.stdin.readline().rstrip())



name1n2 = sorted(list(set(name1) & set(name2)))

print(len(name1n2))
for i in name1n2:
    print(i)
