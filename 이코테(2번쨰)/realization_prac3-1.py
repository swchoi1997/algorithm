def solution(s):
    answer = len(s)    
    length = [] # 최소값을 찾기 위해 만든 list
    length.append(answer) # answer값을 넣지 않으면 s의 길이가 1일 때 오류가 나게 된다.
    for i in range(1, len(s) // 2 + 1):
        sum_str = '' #나눈 문자를 서서히 더할것
        new_s = []
        for a in range(0, len(s), i):
            new_s.append(s[a : a + i]) # 1~len(s) 갯수만큼 나눈것을 list 에 담음
        count = 1 # count 를 1로 만들어줘서 숫자가 1개 있다는 것을 말함
        for b in range(0, len(new_s) - 1):
            if new_s[b] == new_s[b + 1]: # new_s의 b번쨰 와 b+1을 비교 해 나가면서 같으면 count를 증가 시켜줌 // 끝까지 비교를 하기 때문에 중간에 다른게 반복되도 그대로 같이 나아감
                count += 1
            else: # count증가 시키다가 다음에 다른거 만나게되면
                if count >= 2: # count가 2 이상일 때 2_____ 일렇게 마타냄
                    sum_str += str(count) + new_s[b]
                else: # count가 1이라는 것은 반복되는게 없다는 말이기 때문에 그냥 붙여줌
                    sum_str += new_s[b]
                count = 1 # 여기서 count를 1로 만들어줘서 다른게 나오면 1로 초기화
        # 아래 if 문에서는 반복이 되지만 마지막에 다른게 나타나지 않을때 즉 abcabcdede일때 de는 두번 반복되지만 뒤에 다른게 나오지 않기때문에 잴 마지막 문자를 붙여줌
        if count >= 2:
            sum_str += str(count) + new_s[-1]
        else: #바로 위 for 문에서는 제일 마지막 문자가 붙여지지 않는다 그렇기 때문에 제일 마지막 문자열을 뒤에 붙여주는 의미
            sum_str += new_s[-1]
        result = len(sum_str) # 각 for문을 한번 돌았을때 sum_str의 길이
        length.append(result) # sum_str의 길이를 length에 append함
            
    return min(length) # 초기 s의 길이와 줄인 후 s 의 길이를 비교하여 가장 짧은 길이를 return

