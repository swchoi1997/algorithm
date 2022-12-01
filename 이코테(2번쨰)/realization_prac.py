# 럭키 스트레이트

n = list(map(int, input()))

result1, result2 = 0, 0
for i in range(len(n) // 2):
    result1 += n[i]
for i in range(len(n) // 2, len(n)):
    result2 += n[i]   

if result1 == result2:
    print('LUCKY')
else:
    print('READY')


