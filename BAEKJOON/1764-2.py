import sys
input = sys.stdin.readline

data = dict()

n, m = map(int, input().split())


for _ in range(n):
    name = input().rstrip()
    data[name] = 1

data2 = []
for _ in range(m):
    name1 = input().rstrip()

    if name1 in data:
        try:
            data2.append(name1)
        except:
            continue
    
data2.sort()

print(len(data2))
for i in data2:
    print(i)