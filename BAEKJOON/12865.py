import sys
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
backpack  = []
for _ in range(n):
    backpack.append(list(map(int,input().rstrip().split())))

result = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        wei = backpack[i - 1][0]
        val = backpack[i - 1][1]

        if j < wei:
            result[i][j] = result[i - 1][j]
        else:
            result[i][j] = max(result[i-1][j], val + result[i-1][j-wei])


print(result[n][k])



# import sys
# input = sys.stdin.readline

# n, k = map(int,input().rstrip().split())
# backpack = []
# for _ in range(n):
#     backpack.append(list(map(int, input().rstrip().split())))

# backpack = sorted(backpack, key = lambda x : (-x[0], x[1]))

# result = [0 for i in range(n)]

# for i in range(len(backpack)):
#     cnt1 = backpack[i][0]
#     result[i] = backpack[i][1]
#     for j in range(i + 1, len(backpack)):
#         cnt1 += backpack[j][0]
#         if cnt1 <= k:
#             result[i] = max(result[i], result[i] + backpack[j][1])            
#         else:
#             cnt1 -= backpack[j][0]

# print(max(result))


# 10 999
# 46 306
# 60 311
# 33 724
# 18 342
# 57 431
# 49 288
# 12 686
# 89 389
# 82 889
# 16 289

# 6 3
# 1 3
# 1 6
# 1 3
# 1 3
# 1 2
# 1 8