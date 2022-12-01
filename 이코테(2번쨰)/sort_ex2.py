#10814 나이 순 정렬

import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(sys.stdin.readline().rstrip().split()))
    #age, name = sys.stdin.readline().rstrip().split()
    #data.append((age, name))

print(data)
data.sort(key = lambda x : int(x[0]))

for i in range(len(data)):
    print(data[i][0], data[i][1])