import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())

stage = []
for _ in range(n):
    stage.append(list(map(int, input().split())))

hei = 0
inf = 1e9
for i in range(257):
    bin = 0
    bout = 0
    
    for j in range(n):
        for k in range(m):
            if stage[j][k] < i:
                bout += i - stage[j][k]
            else:
                bin += stage[j][k] - i
    inven = bin + b
    if inven < bout:
        continue
    time = bout + bin * 2

    if inf >= time:
        inf = time
        hei = i
print(inf, hei)