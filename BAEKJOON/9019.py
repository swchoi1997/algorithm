from collections import deque
import sys


def D(a):
    newa = a * 2
    if newa > 9999:
        newa = newa % 10000
    
    return newa

def S(a):
    if a == 0:
        newa = 9999
    else:
        newa = a - 1
    return newa
    
def L(a):
    front = (a * 10) % 10000
    back = (a * 10) // 10000
    return front + back

def R(a):
    back = a // 10
    front = (a - (back * 10)) * 1000
    return front + back

def bfs(a, b, visited):
    q = deque()
    q.append([a, '' ])
    visited[a] = True

    while q:
        newa, result = q.popleft()
        if newa == b:
            return result
        
        newa1 = D(newa)
        if visited[newa1] == False:
            visited[newa1] = True
            q.append([newa1, result + 'D'])

        newa1 = S(newa)
        if visited[newa1] == False:
            visited[newa1] = True
            q.append([newa1, result + 'S'])
        
        newa1 = L(newa)
        if visited[newa1] == False:
            visited[newa1] = True
            q.append([newa1, result + 'L'])
        
        newa1 = R(newa)
        if visited[newa1] == False:
            visited[newa1] = True
            q.append([newa1, result + 'R'])



input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    visited = [False] * 10001

    print(bfs(a, b, visited))





########### 이상함 다시하기#############3
# from collections import deque
# import sys
# input = sys.stdin.readline

# def listst(a, aa):
#     numbera = [0] * 4
#     for i in range(aa):
#         numbera[3-i] = a[aa - i - 1]
#     return numbera

# def D(a):
#     newa = int(a) * 2
#     if newa > 9999:
#         newa = newa % 10000
#     newalist = list(str(newa))
#     numbera = listst(newalist, len(newalist))
#     # print(newa, numbera)
#     return str(newa), numbera
    
# def S(a):
#     newa = int(a) - 1
#     if newa < 0:
#         newa = 9999
#     newalist = list(str(newa))
#     numbera = listst(newalist, len(newalist))

#     return str(newa), numbera

# def L(a):
#     lista = list(a)
#     numbera = listst(lista, len(lista))
#     tmp = numbera[0]
#     numbera[0] = numbera[1]
#     numbera[1] = numbera[2]
#     numbera[2] = numbera[3]
#     numbera[3] = tmp
#     # print(numbera)
#     newa = ''
#     for i in numbera:
#         newa += str(i)
#     return newa, numbera

# def R(a):
#     lista = list(a)
#     numbera = listst(lista, len(lista))
#     tmp = numbera[3]
#     numbera[3] = numbera[2]
#     numbera[2] = numbera[1]
#     numbera[1] = numbera[0]
#     numbera[0] = tmp
#     # print(numbera)
#     newa = ''
#     for i in numbera:
#         newa += str(i)

#     return newa, numbera


# def bfs(a, b, numbera, visited):
#     q = deque()
#     q.append([a, numbera, ""])
#     visited.add(a)
#     while q:
#         newa, numbera, check1 = q.popleft()
#         if int(newa) == int(b):
#             return check1
#         newa1, numbera = D(newa)
#         if newa1 not in visited:
#             visited.add(newa1)
#             q.append([newa1, numbera, check1 + "D"])

#         newa1, numbera = S(newa)
#         if newa1 not in visited:
#             visited.add(newa1)
#             q.append([newa1, numbera, check1 + "S"])

#         newa1, numbera = L(newa)
#         if newa1 not in visited:
#             visited.add(newa1)
#             q.append([newa1, numbera, check1 + "L"])

#         newa1, numbera = R(newa)
#         if newa1 not in visited:
#             visited.add(newa1)
#             q.append([newa1, numbera, check1 + "R"])
#         # print(q)



# t = int(input())
# for _ in range(t):
#     a, b = map(str, input().split())
#     alist = list(a)

#     numbera = listst(alist, len(alist))

#     visited = set()

#     print(bfs(a, b, numbera, visited))
    

    


    
