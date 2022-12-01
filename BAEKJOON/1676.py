n = int(input())

value = 1
for i in range(1, n + 1):
    value *= i
    
valuelist = list(str(value))

if '0' not in valuelist:
    print(0)
    exit()

cnt = 0
for i in range(len(valuelist) -1, 0 , -1):
    if valuelist[i] != '0':
        print(cnt)
        exit()
    cnt += 1