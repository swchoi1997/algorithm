import sys
input = sys.stdin.readline

def bs(home, c, start, end):
    global result
    while start <= end:
        cnt = 1 
        
        mid = (start + end) // 2
        a = home[0]
        for i in range(1, len(home)):
            if home[i] >= mid + a:
                cnt += 1
                a = home[i]

        if cnt >= c:
            start = mid + 1
            result = mid
        elif cnt < c:
            end = mid - 1

n, c = map(int,input().rstrip().split())
home = []
for _ in range(n):
    home.append(int(input().rstrip()))

home.sort()
if c == 2:
    print(home[-1] - home[0])
    exit()
result = 0
a = bs(home, c, 1, home[-1] - home[0])

print(result)
