import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

left, right = 0, n - 1

check1 = a[left]
check2 = a[right]

result = sys.maxsize

while left < right:
    tmp = a[left] + a[right]

    if abs(tmp) < result:
        result = abs(tmp)
        check1, check2 = a[left], a[right]

    if tmp < 0:
        left += 1
    else:
        right -= 1
        
    
print(check1, check2)    

