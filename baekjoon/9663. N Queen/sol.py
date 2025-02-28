
def dfs(x, y):
    global cnt
    if y == n:
        return
    if x == n:
        cnt += 1
        return

    if check_queen(x, y):
        visited_y[y] = 1
        visited_diag[y - x + n - 1] = 1
        visited_diag_res[x + y] = 1
        dfs(x + 1, 0)
        visited_y[y] = 0
        visited_diag[y - x + n - 1] = 0
        visited_diag_res[x + y] = 0

    dfs(x, y + 1)
    return
def check_queen(x, y):
    if visited_y[y] or visited_diag[y - x + n - 1] or visited_diag_res[x + y]:
        return False
    return True

n = int(input())
visited_y = [0] * n
visited_diag = [0] * (n*2-1)
visited_diag_res = [0] * (n*2-1)
cnt = 0
dfs(0, 0)

print(cnt)