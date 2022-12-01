#곱하기 혹은 더하기

number = list(map(int, input()))
result = 0
result += number[0]

for i in range(1, len(number)):
    if result == 0: # 처음 값이 0 인 경우와 계속해서 0이 나오는 경우 에는 그 다음 값을 더함
        result += number[i]
    else:
        if number[i] == 0:
            result += number[i]
        else:
            result *= number[i]

print(result)