import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    case = dict()
    for _ in range(n):
        a, b = map(str, input().rstrip().split())
        if b in case:
            case[b] += 1
        else: case[b] = 1
    case = list(case.values())
    result = 1
    for i in case:
        result *= (i + 1)


    print(result - 1)

##{1,2,3}{4,5}{6} 이 있으면 아래와 같은 조합이 나와야함
# 1,2,3,4,5,6
# 14 15 16 24 25 26 34 35 36 46 56
# 146 156 246 256 346 356
# 4*3*2 -1 하면됨