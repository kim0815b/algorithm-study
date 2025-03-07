def dfs(idx=0):
    global max_val
    if idx == n ** 2:   #  배열 최대값을 넘으면
        cnt = cnt_bishop()
        if max_val < cnt:
            max_val = cnt
        return
    x = idx // n
    y = idx % n
    if arr[x][y]:   #놓을 수 있으면      흰색
        dia_idx = n - 1 - (x - y)
        aniti_idx = x + y
        if bishop_check(x, y):  #경우의 수
            diagonal[dia_idx] = 1
            anti_diagonal[aniti_idx] = 1
            bishop[x][y] = 1    #놓고
            dfs(idx + 1)
            # 백트래킹
            bishop[x][y] = 0  # 빼고
            diagonal[dia_idx] = 0
            anti_diagonal[aniti_idx] = 0
            dfs(idx + 1)
        else:
            dfs(idx + 1)
    else:   # 못놓으면 그냥
        dfs(idx + 1)

def bishop_check(x, y):
    dia_idx = n - 1 - (x - y)
    aniti_idx = x + y
    if diagonal[dia_idx] or anti_diagonal[aniti_idx]:
        return False
    return True

def cnt_bishop():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bishop[i][j]:
                cnt += 1
    return cnt

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
bishop = [[0] * n for _ in range(n)]
diagonal = [0] * (n * 2 - 1)
anti_diagonal = [0] * (n * 2 - 1)
max_val = float('-inf')

dfs()
print(max_val)
