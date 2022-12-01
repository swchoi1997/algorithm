import sys
input = sys.stdin.readline
n = int(input())
x1 = list(map(int,input().rstrip().split()))
x2 = sorted(set(x1))
x3 = dict()
for i in range(len(x2)):
    x3[x2[i]] = i
for i in x1:
    print(x3[i], end = ' ')
