#문자열 압축

def solution(s):
    answer = len(s)
    count = 0

    for i in range(1, (len(s) // 2 ) + 1):
        compressed = ''
        new_list = s[0:i]
        count = 1
        for a in range(i, len(s), i):
            if new_list == s[a:a+i]:
                count += 1
            else:
                compressed += str(count) + new_list if count >= 2 else new_list
                new_list = s[a:a+i]
                count = 1

            compressed += str(count) + new_list if count >= 2 else new_list
            answer = min(answer,len(compressed))        

        return answer


    

solution('abcabcabcabcdededededede')
