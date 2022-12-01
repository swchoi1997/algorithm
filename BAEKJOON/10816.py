import sys
input = sys.stdin.readline

def binary_search(target, num1, start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2

        if num1[mid] == target:
            count += 1
            num1.remove(target)
            end -= 1             
        elif num1[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return count

n = int(input())
num1 = list(map(int, input().split()))
num1.sort()
m = int(input())
num2 = list(map(int, input().split()))

num3 = []
for i in num2:
    target = i
    num3.append(binary_search(target, num1, 0, len(num1) - 1))

for i in num3:
    print(i, end = ' ')

    ########시 간 초 과#######