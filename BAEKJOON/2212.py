
n = int(input())
m = int(input())
sence = list(map(int,input().split()))
sence.sort()

check = []
for i in range(len(sence) - 1):
    check.append(sence[i + 1] - sence[i])

newCheck = sorted(check, reverse=True)

newCheck = newCheck[:m-1]

result = 0
num = sence[0]
for i in range(n - 1):
    if check[i] in newCheck:
        newCheck.remove(check[i])
        result += sence[i] - num
        num = sence[i + 1]
result += sence[-1] - num

print(result)
