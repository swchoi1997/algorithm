import sys
input = sys.stdin.readline

def binary_serach(a,target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return 1
        elif a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int,input().split()))
a.sort()
m = int(input())
b = list(map(int,input().split()))

for i in b:
    target = i
    print(binary_serach(a, target, 0 , n-1))

