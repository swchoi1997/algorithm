from collections import deque
import sys
input = sys.stdin.readline
check = ['P','P','A','P']

ppap = deque(list(map(str, input().rstrip())))


new_ppap = []
while ppap:
    word = ppap.popleft()
    new_ppap.append(word)

    if new_ppap[-4:] == check:
        for _ in range(3):
            new_ppap.pop()
              
    
str1 = ''
for i in new_ppap:
    str1 += i

if str1 == 'P' or str1 == 'PPAP':
    print('PPAP')
else:
    print('NP')