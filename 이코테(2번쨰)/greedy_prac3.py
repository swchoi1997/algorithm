# 문자열 뒤집기

_list = list(map(int, input()))

count =0

for i in range(1, len(_list)):
    if _list[i - 1] != _list[i]:
        if _list[0] != _list[i]:
            count +=1

print(count)