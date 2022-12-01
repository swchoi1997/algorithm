# 볼링공 고르기

import timeit

n, m = map(int, input().split())
ball = list(map(int, input().split()))

start_time = timeit.default_timer()

count = 0

#1번 풀이

for i in range(len(ball)):
     for k in range(i, len(ball)):
         if ball[i] != ball[k]:
             count += 1

print(count)

terminate_time = timeit.default_timer()

print(terminate_time - start_time)



# 2번 풀이

# a = (n * (n -1)) // 2

# for i in range(len(ball)):
#     for k in range(i, len(ball)):
#         if ball[i] == ball[k] and i != k:
#             count += 1

# print(a - count)