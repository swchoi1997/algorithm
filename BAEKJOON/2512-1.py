import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int,input().rstrip().split()))
budget.sort()
total_budget = int(input())

start, end = 1, budget[-1]

while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for i in budget:
        if i < mid:
            sum_budget += i
        else:
            sum_budget += mid

    if sum_budget > total_budget:
        end = mid - 1
    else:
        start = mid + 1


if sum(budget) <= total_budget:
    print(budget[-1])
else:
    print(end)