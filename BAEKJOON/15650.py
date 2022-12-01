from itertools import combinations

n ,m = map(int,input().split())

num = [i for i in range(1, n + 1)]

n_num = list(combinations(num, m))

for i in n_num:
    for j in range(len(i)):
        print(i[j], end = " ")
    print()