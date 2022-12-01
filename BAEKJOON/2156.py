n = int(input())

juice = []
for _ in range(n):
    juice.append(int(input()))
# print(juice)
if len(juice) <= 2:
    print(sum(juice))
    exit()


result = [0] * n
result[0], result[1] = juice[0], juice[1] + juice[0]
result[2] = max(juice[0]+juice[1], juice[0]+juice[2], juice[1]+ juice[2])

for i in range(3, len(juice)):
    result[i] = max(result[i - 1], result[i - 2] + juice[i], result[i - 3] + juice[i-1] + juice[i])
print(max(result))
