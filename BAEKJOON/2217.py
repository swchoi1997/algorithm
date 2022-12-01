
import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort(reverse=True)

result = rope[0]
for i in range(1, len(rope)):
    
    if rope[i] * (i + 1) > result:
        result = rope[i] * (i + 1)
    

print(result)      
    