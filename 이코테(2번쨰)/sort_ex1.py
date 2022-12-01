#단어 정렬 백준 1181
# import sys

# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().rstrip() for _ in range(n)]

# datas = list(set(data))
# datas.sort(key = lambda x :(len(x), x))

# for a in datas:
#     print(a)

#단어 정렬 백준 1181
import sys

input = sys.stdin.readline
n = int(input())
data = [input().rstrip() for _ in range(n)]

datas = list(set(data))
datas.sort(key = lambda x :(len(x), x))

for a in datas:
    print(a)