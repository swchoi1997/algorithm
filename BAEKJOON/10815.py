import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
m = int(input())
checkNum = list(map(int,input().split()))
num.sort()

for i in checkNum:
    start, end = 0, len(num) - 1
    TF = False
    while start <= end:
        mid = (start + end) // 2

        if num[mid] == i:
            print(1, end = ' ')
            TF = True
            break
        elif num[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

    if not TF:
        print(0, end = ' ')
        