from itertools import permutations

n = int(input())
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
allNum = list(permutations(num, 3))

youngsu = []
result = []
for _ in range(n):
    ques, s, b = map(str,input().split())
    youngsu.append([ques, int(s), int(b)])



for number in allNum:
    check = 0
    for j in range(n):
        ques, sk, bl = youngsu[j][0], youngsu[j][1], youngsu[j][2]
        strike, ball = 0, 0
        
        for i in range(3):
            if ques[i] == number[i]:
                strike += 1
            else:
                if ques[i] in number:
                    ball += 1
        if strike == sk and ball == bl:
            check += 1

    if check == n:
        result.append(number)    
print(len(result))