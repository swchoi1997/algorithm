import heapq, sys
input = sys.stdin.readline

n = int(input())
result = 0
ns = []
for _ in range(n):
    ns.append(int(input()))

def heapsort(ns):
    h = []
    result = [] 
    for i in ns:
        heapq.heappush(h, i)  
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

heapns = heapsort(ns)
while True:
    if len(heapns) == 1:
        break
    num1 = heapq.heappop(heapns)
    num2 = heapq.heappop(heapns)
    result += (num1 + num2)
    heapq.heappush(heapns, num1 + num2)
    
print(result)