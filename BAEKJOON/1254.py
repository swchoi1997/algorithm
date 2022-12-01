import sys
input = sys.stdin.readline
s = list(map(str, input().rstrip()))

len_s = len(s)

if len_s == 1:# 길이가 1이면 어차피 팰린트롬이기 때문에 무조건 출력 후 끝
    print(1)
    exit()

def checkt(cnt): # 팰린트롬이 형성되는 곳 위치를 확인해야함
    start = cnt
    end = len_s - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

cnt = 0

while not checkt(cnt):
    cnt += 1

print(len_s + cnt)

# 어디서부터 팰린트롬이 형성되는지 확인하는게 포인트임
# 주어진 문자열에서 팰린트롬이 형성하는 위치를 알아야 나머지 문자들을 더해서 팰린트롬을 형성할 수 있음