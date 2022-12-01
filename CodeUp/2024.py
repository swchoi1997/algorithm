
#숫자를 한글로 변환
#https://codeup.kr/problem.php?id=2024

number1 = {1: "일", 2 : "이", 3 : "삼", 4 : "사", 5 : "오", 6 : "육", 7 : "칠", 8 : "팔", 9 : "구"}
number2 = {10 : "십", 100:"백", 1000: "천", 10000:"만", 100000000:"억"}

def numToHan(number):
    tmpNum = number
    for i in reversed(number2): #억단위 부터 탐색
        if i > tmpNum: # 현재 숫자가 기준숫자보다 작은 경우는 더 작은 단위가 필요하므로 continue
            continue
        elif i == tmpNum: # 만약 기준 단위랑 똑같다면 단위 출력하고 return
            if number2[i] == "억": #억은 일억이라고 보통 이야기하니까 억 이상일때만 일억 출력 일조도 같은 맥락
                print("일", end = '')
            print(number2[i], end = '')
            return
        else: # 그 이외에 나머지는
            tmp = tmpNum // i # 123,450,000,000 같은경우 1234억 이니까 1234 를 만들어주고
            tmpNum = tmpNum % i # 위에 숫자를 버린 나머지수  5천만

            if tmp >= 10: # 1234억의 경우 1234는 천 이백 삼삽 사로 다시 할 수 있으니까 numToHan을 통해 재귀돌림
                numToHan(tmp)
                print(number2[i], end= '') # 재귀가 리턴될 때 단위를 출력
            else: # 만약 9억일때 라고 생각하면 tmp가 10보다 작으니까
                if tmp != 1: # 10억의 경우 일십억이 아니라 십억이니까 1은 출력하지않고 그 나머지 숫자만 
                    print(number1[tmp], end = '')
                print(number2[i], end= '') # 그리고 단위 출력

        # 처리하고 남은 숫자 
        if 0 < tmpNum < 10:
            print(number1[tmpNum], end = '')
        elif tmpNum == 10: # 110 과 같이 백 십을 출력해야할때 남은숫자가 10이면 그냥 십만 출력하도록 
            print("십" , end = '')
        else: # 123,450,000,000 은 1234억을 출력하고 5천만이 남았으니까 50000000에 대해서 다시 재귀
            numToHan(tmpNum)
        return

number = int(input())

if number < 10: #숫자가 10 미만일 때는 그냥 간단하게 처리해줌
    if number == 0:
        print("영")
    else:
        print(number1[number])
else: # 숫자가 10 이상일때
    numToHan(number)



    

# a = "영일이삼사오육칠팔구"
# b = "영십백천만십백천억십"


# def number_to_string(num):
#     answer = ""
#     num = str(num)
#     length = len(num)
#     for i in range(length):
#         int1 = int(num[i])
#         if int1 == 0 and length > 1:
#             continue
#         answer += a[int1]
#         temp = length - i - 1
#         if temp == 0:
#             continue
#         suffix = ""
#         if 5 <= temp <= 7 and num[i:i + (temp - 3)] == num[i] + "0" * (temp - 4):
#             suffix = "만"
#         elif length == 10 and temp == 9 and num[i: i + 2] == num[i] + "0":
#             suffix = "억"
#         answer += b[length - i - 1] + suffix
#     print(answer)


# x = input()
# number_to_string(x)    


# #숫자를 한글로 변환

# number1 = {1: "일", 2 : "이", 3 : "삼", 4 : "사", 5 : "오", 6 : "육", 7 : "칠", 8 : "팔", 9 : "구"}
# number2 = {10 : "십", 100:"백", 1000: "천", 10000:"만", 100000000:"억"}


# def numToHan(number):
#     tmpNum = number
#     for i in reversed(number2):
#         if i > tmpNum: # 기준 숫자보다 큰 경우 
#             continue
#         elif i == tmpNum:
#             print("일", end = '')
#             print(number2[i], end = '')
#             return
#         else:
#             tmp = tmpNum // i
#             tmpNum = tmpNum % i

#             if tmp >= 10:
#                 numToHan(tmp)
#                 if tmp == 1:
#                     print(number2[i], end= '')
#                 else:
#                     print(number2[i], end= '')
#             else:
#                 if tmp == 1:
#                     print(number1[tmp], end = '')
#                     print(number2[i], end= '')
#                 else:
#                     print(number1[tmp], end = '')
#                     print(number2[i], end= '')

            
#         if tmpNum < 10 and tmpNum > 0:
#             print(number1[tmpNum], end = '')
#         elif tmpNum == 10:
#             print("일십" , end = '')
#         else:
#             numToHan(tmpNum)
#         return

# number = int(input())
# if number < 10:
#     if number == 0:
#         print("영")
#     else:
#         print(number1[number])
# else:
#     numToHan(number)



    