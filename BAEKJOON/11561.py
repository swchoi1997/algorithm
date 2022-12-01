import sys

input = sys.stdin.readline


def jump(start, end):
    final = end
    while start <= end:
        mid = (start + end) // 2

        if mid*(mid + 1) // 2 <= final:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

n = int(input().rstrip())

for _ in range(n):
    final = int(input().rstrip())
    if final == 1:
        print(1)
        continue
    
    print(jump(1, final))