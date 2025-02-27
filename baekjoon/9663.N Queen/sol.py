def dfs(arr, y, befor_x):
    global cnt
    if y == n-1:
        # print([j for i in arr for j in i].count(1))
        if [j for i in arr for j in i].count(1) == n-1 and check_queen_attack(arr, befor_x, y):
            cnt += 1
        return

    for x in range(n):  #가로행
        if check_queen_attack(arr, x, y):
            arr[y][x] = 1
            dfs(arr, y+1, x)
            arr[y][x] = 0

def check_queen_attack(arr, x, y):
    dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    if x == n-1 and y == n-1:
        print('here')
    if x == 3 and y == 2:
        print('here')
    for i in range(1, n+1):  #n만큼 탐색
        for dx, dy in dxy:  #8방향
            nx = x + dx
            ny = y + dy
            if nx > n-1 or nx < 0 or ny > n-1 or ny < 0:
                continue
            if arr[ny][nx]:
                return False
    return True
cnt = 0
n = int(input())
arr = [[0] * n for _ in range(n)]
dfs(arr,0,0)

print(cnt)