n = int(input())

cnt = 0
for _ in range(n):
    word = list(str(input()))

    word_count =  [0] * 31
    
    word_count[ord(word[0]) - 97 ] += 1 # happy h

    for i in range(1, len(word)):
        if word[i-1] == word[i]: 
            continue
        else:
            word_count[ord(word[i])- 97] += 1
    
    cnt2 = 0
    for i in word_count:
        if i > 1:
            continue
        elif i <= 1:
            cnt2 += 1
        
    if cnt2 == 31:
        cnt += 1

print(cnt)