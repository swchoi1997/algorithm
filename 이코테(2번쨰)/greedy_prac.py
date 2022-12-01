#모험가 길드
 #1회차
# m = int(input())# 모험가 수 입력
# k = list(map(int, input().split())) # 공포도 입력
# k.sort()
# result = 0
# count = 0
# for i in k:
#     count += 1
#     if count >= i:
#         result +=1
#         count = 0

# print(result)


# 모든 모험가를 다 넣을 필요는 없기 때문에, 공포도가 같은 것 끼리 뭉쳐놓으면 됨(공포도와 인원수 맞게)
# 결국 1 2 2 3 3 3 4 4 4 4  이렇게 뭉쳐지게 되고 남은건 신경 안써도 됨!! 조건에 몇명의 모험가는
# 마을에 남아도 된다고 했기때문임!, 

#2회차

n = int(input()) # 모험가의 수
m = list(map(int,input().split()))
m.sort()
result = 0
count = 0

for i in m:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)