# 자물쇠와 열쇠

def rotate_90(key): # 90 도 돌리는 함수
    n = len(key)
    key_90 = [[0] * n for _ in range(n)] #90 도 돌아간 값을 저장할 공간을 생성
    for a in range(n):
        for b in range(n):
            key_90[b][n - 1 - a] = key[a][b]
    return key_90

    # 90도 돌아간 것 알고리즘
    # (0,0) (0,1) (0,2) - > (0,2) (1,2) (2,2)
    # (1,0) (1,1) (1,2) - > (0,1) (1,1) (2,1)
    # (2,0) (2,1) (2,2) - > (0,0) (1,0) (2,0)
    # 90도 회전을 시켰을 때 행의 값이 열의 값으로 변경되고
    # 열의 값은 (행(열)의 길이 - 1 - 행 값)이 나오게 된다
    # 이를 이용하여 for문을 두번 돌려 모든 key 값을 90도씩 회전 할 수 있게 해준다!!!

def check(new_lock): # lock 에 key 값을 더했을때 모든 값이 1이 되는지 확인하는 함수
    l_lock = len(new_lock) // 3 # 원래 lock 에서 3배를 해줬기 때문에 3으로 나눠줌
    for i in range(l_lock, l_lock * 2): # 전체 3n이 된 list에서 n 번째부터 원래 list 크기만큼 확인할 수 있음
        for j in range(l_lock, l_lock * 2):
            if new_lock[i][j] != 1: #모든 값이 1이 아니라면 False리턴
                return False
    return True

def solution(key, lock):
    answer = True
    # lock 리스트 3배로 늘리기 + 늘린 리스트 가운데 원래 리스트의 값 넣기
    l_key = len(key)
    l_lock = len(lock)
    new_lock = [[0] * (l_lock * 3) for _ in range(l_lock * 3)] # lock크기의 3배로 늘려준 list를 새로 생성함
    for i in range(l_lock):
        for j in range(l_lock):
            new_lock[l_lock + i][l_lock + j] = lock[i][j] # 새로운 list에 원래 lock값을 넣어줌(가운데에)

    # key 값을 리스트에 더해가면서 lock 값이 전부 1이 되는지 확인하기
    for rotate in range(4): # 360도 회전을 해야하기 때문에 90 도씩 4번 확인해줌
        for a in range(l_lock * 2): # 제일 끝에 걸치는 부분까지 생각해주면 됨
            for b in range(l_lock * 2):
                for c in range(l_key):
                    for d in range(l_key):
                        new_lock[a + c][b + d] += key[c][d]
                        
                # 열쇠가 맞으면 True 반환
                if check(lock) == True:
                    return True
                # 열쇠가 틀리면 원상복귀
                for e in range(l_key):
                    for f in range(l_key):
                        new_lock[a + e][b + f] -= key[e][f]      
        # 90 도 회전 한 값을 key 값으로 갱신해줌                       
        key = rotate_90(key)                             
    return False           

a = solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]])
print(a)