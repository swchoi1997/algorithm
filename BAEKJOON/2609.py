n, m = map(int, input().split())
a, b = max(n,m), min(n,m) # 유클리드 호제법을 사용하기위해 더 큰값을 나눔

while True:
    r = a % b
    if r == 0:
        break
    a, b = b, r

# b 는 최대공약수
print(b)
print(n * m // b)



