import sys
input = sys.stdin.readline
limit = 1e9

n ,m = map(int, input().split())
card = list(map(int, input().split()))

new_card = []
for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            result = card[i] + card[j] + card[k]
            new_card.append(result)
            result = 0
            
for a in range(len(new_card)):
    new_card[a] = m - new_card[a]
    if new_card[a] < 0:
        new_card[a] = limit

print(m - min(new_card))