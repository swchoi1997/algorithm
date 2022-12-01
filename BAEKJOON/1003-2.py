import sys
input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    num = int(input().rstrip())
    if num == 0:
        print("1 0")
        continue
    fibo = [[0] * 2 for i in range(num + 1)]
    fibo[0], fibo[1] = [1, 0], [0, 1]
    
    for i in range(2, len(fibo)):
        fibo[i][0] = fibo[i-1][0] + fibo[i -2][0]
        fibo[i][1] = fibo[i-1][1] + fibo[i -2][1]

    print(fibo[num][0], fibo[num][1])