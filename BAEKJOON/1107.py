from itertools import product

num  = [0,1,2,3,4,5,6,7,8,9] #리모컨 
first = 100 

INF = 10e9

n = int(input())
m = int(input())
if m != 0 :
    num_mov = list(map(int, input().split()))

    for i in num_mov: 
        num.remove(i)

result = INF
result1 = 0
pre_num = 0

for i in range(1, 7):
    number = list(product((num), repeat = i))
    
    for i in number:
        new_num = ''
        
        for j in range(len(i)):
            new_num += str(i[j])
        
        a = n - int(new_num)
        result = min(result, abs(a)) # n 5457 5458  5600  result = 1 
        
        if result1 != result: 
            pre_num = int(new_num)
        result1 = result

cnt1 = len(str(pre_num)) + result

cnt2 = 0
while True:
    if n > first:
        first += 1
    elif n < first:
        first -= 1
    elif n == first:
        break
    cnt2 += 1


print(min(cnt1, cnt2))