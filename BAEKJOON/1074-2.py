import sys
sys.setrecursionlimit(1000000)

N, r, c = map(int,input().split())
cnt = 0
def dq (x ,y ,N):
    global cnt
    newr = r - x
    newc = c - y

    if N == 2:
        for i in range(2):
            for j in range(2):
                if i == newr and j == newc:
                    print(cnt)
                    break
                cnt += 1
    else:
        if newr < N // 2 and newc < N // 2:
            dq(x, y, N // 2)
        cnt += (N // 2) ** 2
        if newr < N // 2 and newc >= N // 2:
            dq (x, y + (N // 2), N //2)
        cnt += (N // 2) ** 2
        if newr >= N // 2 and newc < N // 2:
            dq(x + (N // 2), y, N // 2)
        cnt += (N // 2) ** 2
        if newr >= N//2 and newc >= N // 2:
            dq(x + (N // 2), y + (N // 2), N // 2)
        cnt += (N // 2) ** 2



dq(0, 0, 2 ** N)