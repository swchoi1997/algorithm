n = int(input())
case = [[0] * 10 for i in range(n)]
case[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, len(case)):
    for j in range(len(case[i])):
        if j == 0 :
            case[i][j] = case[i - 1][1]
        elif j == 9:
            case[i][j] = case[i - 1][8]
        else:
            case[i][j] = case[i - 1][j - 1] + case[i -1][j + 1]

print(sum(case[n - 1]) % 1000000000)
