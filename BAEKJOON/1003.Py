t = int(input())
for _ in range(t):
    f = int(input())
    if f == 0:
        print("1", "0")
        continue
    if f == 1:
        print("0", "1")
        continue

    fibo = [[0, 0] for _ in range(f + 1)]
    fibo[0] = [1, 0]
    fibo[1] = [0, 1]
    # print(fibo)
    for i in range(2, len(fibo)):
        fibo[i][0] = fibo[i -1][0] + fibo[i -2][0]
        fibo[i][1] = fibo[i -1][1] + fibo[i -2][1]

    print(fibo[-1][0], fibo[-1][1])    
    