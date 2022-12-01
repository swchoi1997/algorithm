import sys
input = sys.stdin.readline
a, b = map(str, input().rstrip().split())
a, b = list(a), list(b)

# a는ㄴ b보다 작거나 같다.

cut = len(b) - len(a)
cnt = 0
for i in range(cut + 1):
    cnt1 = 0
    for j in range(len(a)):

        if b[j + i] == a[j]:
            cnt1 += 1

    cnt = max(cnt, cnt1)

print(len(b) - (cnt + cut))
