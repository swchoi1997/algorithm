import sys
input = sys.stdin.readline
t = int(input())
cnt = 0
while cnt < t:
    n = int(input())
    arr =[]
    for _ in range(n):
        arr.append(list(map(int,input().rstrip().split())))

    arr1 = sorted(arr, key = lambda x: x[0])
    # print(arr1)
    cnt1 = 1
    std = arr1[0][1]
    for i in range(1, len(arr1)):
        if arr1[i][1] < std:
            cnt1 += 1
            std = arr1[i][1]
    print(cnt1)
    cnt += 1


# 1
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1