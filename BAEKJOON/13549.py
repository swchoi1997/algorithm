from collections import deque

su, bro = map(int,input().split())

loc = [-1] * 100001

q = deque()
q.append([su, 0])
loc[su] = 0
result = []
while q:
    curr, time = q.popleft()
    
    # if curr * 2 >= len(loc) or curr + 1 >= len(loc) or curr - 1 < 0:
    #     continue
    

    if curr * 2 < len(loc) and loc[curr * 2] == -1:
        q.append([curr * 2, time])
        loc[curr * 2] = time

    if curr - 1 >= 0 and loc[curr - 1] == -1:
        q.append([curr - 1, time + 1])
        loc[curr - 1] = time+ 1

    if curr + 1 < len(loc) and loc[curr + 1] == -1:
        q.append([curr + 1, time+ 1])
        loc[curr + 1] = time+ 1

print(loc[bro])





        

    # if loc[curr * 2] == -1:
    #     q.append([curr * 2, time])
    #     loc[curr * 2] = time
    # elif loc[curr * 2] != -1 and loc[curr * 2] >= loc[curr]:
    #     q.append([curr * 2, time])
    #     loc[curr * 2] = time

    # if loc[curr - 1] == -1:
    #     q.append([curr - 1, time + 1])
    #     loc[curr - 1] = time+ 1
    # elif loc[curr * 2] != -1 and loc[curr - 1] >= loc[curr]:
    #     q.append([curr - 1, time+ 1])
    #     loc[curr - 1] = time+ 1

    # if loc[curr + 1] == -1:
    #     q.append([curr + 1, time+ 1])
    #     loc[curr + 1] = time+ 1
    # elif loc[curr + 1] != -1 and loc[curr + 1] >= loc[curr]:
    #     q.append([curr + 1, time+ 1])
    #     loc[curr + 1] = time+ 1

# print(loc[bro])

#  if curr * 2 >= len(loc):
#         if curr + 1 >= len(loc):
#             q.append([curr - 1, time + 1])
#             loc[curr - 1] = time + 1
#         else:
#             loc[curr + 1], loc[curr - 1] = time + 1, time + 1
#             q.append([curr + 1, time + 1])
#             q.append([curr - 1, time + 1])
#     else: 