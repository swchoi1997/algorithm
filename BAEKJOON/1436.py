n = int(input())

count = 0
sss = 666

while True:
    if '666' in str(sss):
        count += 1
        if count == n:
            print(sss)
            break
    sss += 1

