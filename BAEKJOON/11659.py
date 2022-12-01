import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = [0] + list(map(int,input().rstrip().split()))

for i in range(1, n + 1):
    num[i] = num[i] + num[i - 1]

for i in range(m):
    a, b = map(int,input().split())
    print(num[b] - num[a - 1])
    