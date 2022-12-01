import sys
input = sys.stdin.readline

n ,m  = map(int,input().split())
result = [{} for _ in range(m)]
dna = [str(input().rstrip()) for _ in range(n)]

for i in dna:
    for j in range(len(i)):
        if i[j] in result[j]:
            result[j][i[j]] += 1
            continue
        result[j][i[j]] = 1
for i in result:
    print(i)
result1 = ''
result2 = 0    
for i in result:
    a = sorted(i.items(), key=lambda x: (-x[1], x[0]))
    result1 += a[0][0]
    result2 += (n - a[0][1])
    
print(result1)
print(result2)