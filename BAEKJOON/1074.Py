n, r, c = map(int,input().split())

cnt = 0
def dq(x, y, n): # n ==3 이면 8 이 넘어옴
    global cnt
    newr = r - x
    newc = c - y
    
    if n == 2:
        for i in range(x, x + n):
            for j in range(y, y + n):
                if i == r and j == c:
                    print(cnt)
                    exit()
                cnt += 1
    else:
        if newr < n // 2 and newc < n // 2:
            dq(x, y, n // 2)
        cnt += (n//2)**2
        if newr < n // 2 and newc >= n //2:
            dq(x, y + n // 2, n // 2)
        cnt += (n//2)**2
        if newr >= n // 2 and newc < n //2:
            dq(x + n // 2, y, n // 2)
        cnt += (n//2)**2
        if newr >= n // 2 and newc >= n //2:
            dq(x + n // 2, y + n // 2, n // 2)
        cnt += (n//2)**2

dq(0, 0, 2 ** n)
