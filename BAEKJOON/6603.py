import sys
from itertools import combinations
while True:
    arr = list(map(int,input().rstrip().split()))
    if arr[0] == 0:
        exit()

    arr2 = arr[1:]
    arr3 = list(combinations(arr2, 6))

    for i in range(len(arr3)):
        for j in range(len(arr3[i])):
            print(arr3[i][j], end = " ")
        print()
    print()    

###DFS로 풀기