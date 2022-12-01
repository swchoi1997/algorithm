n = int(input())

result = []
for i in range(n):
    a = input()
    result.append(list(a))

count = 0
count_result = [0] * n
for i in range(n):
    for j in range(len(result[i])):
        if result[i][j] == 'O':
            count += 1
        elif result[i][j] == 'X':
            count = 0
        count_result[i] += count
    count = 0

for i in count_result:
    print(i)