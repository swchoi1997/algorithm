#큰 수의 법칙

n, m, k = map(int, input().split())
value = list(map(int, input().split()))

value.sort()

first = value[-1]
second = value[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1
    

print(result)

