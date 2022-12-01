import sys
input = sys.stdin.readline

n = int(input())

_time = []

for _ in range(n):
    a, b = map(int, input().split())
    _time.append([a,b])

_time.sort(key = lambda x : (x[1], x[0]))

end_time =_time[0][1]
cnt = 1
for i in range(1, len(_time)):
    if _time[i][0] < end_time:
        continue
    else:
        cnt+= 1
        end_time = _time[i][1]
    

print(cnt)