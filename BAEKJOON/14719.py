h, w = map(int,input().split())
world = list(map(int,input().split()))
result = 0

left, right = 0, w - 1
check1, check2 = world[left], world[right]

while left < right:
    check1 = max(check1, world[left])
    check2 = max(check2, world[right])

    if check2 >= check1:
        result += check1 - world[left]
        left += 1
    else:
        result += check2 - world[right]
        right -= 1

print(result)

    
