import sys
sys.stdin = open('4875_input (1).txt','r')
def dfs(x, y, before_x, before_y):
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return
    if visited[x][y] or arr[x][y] == 1:
        return
    visited[x][y] = 1
    if arr[x][y] == 3:
        global ans
        ans = 1
        return
    dfs(x + 1, y, x, y)
    dfs(x, y + 1, x, y)
    dfs(x - 1, y, x, y)
    dfs(x, y - 1, x, y)


#################################
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    ans = 0
    visited = [[0] * n for _ in range(n)]
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start_x, start_y = i, j
    dfs(start_x, start_y, -1, -1)

    print(f'#{tc} {ans}')
