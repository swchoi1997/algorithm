from itertools import permutations

n ,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

num = list(permutations(num, m))

for i in num:
    for j in i:
        print(j, end = ' ')
    print()