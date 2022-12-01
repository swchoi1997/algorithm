import sys
input = sys.stdin.readline
def bs(arr1, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == arr1[mid]:
            return 1
        elif target > arr1[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0
        
t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    m = int(input())
    arr2 = list(map(int,input().split()))

    arr1.sort()

    for i in arr2:
        a = bs(arr1, i, 0 , n - 1)
        print(a)
