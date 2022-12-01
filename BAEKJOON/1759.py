from itertools import combinations
l,c = map(int,input().split())

aeiou = ['a','e','i','o','u']

pw = list(map(str,input().split()))
pw.sort()

pw2 = list(combinations(pw, l))

for i in pw2:
    result = ''
    cnt = 0
    for j in i:
        if j in aeiou:
            cnt += 1
        result += j
    if cnt > 0 and cnt <= (l-2):
        print(result)
    
