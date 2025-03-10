def dfs(x, y, cnt=0):
    global max_val
    if x + y >= 2 * n - 2 and y == n:
        if max_val < cnt:
            max_val = cnt
        return
    if n * 2 - (x + y + 2) < max_val - cnt:
        return
    if y > n - 1:
        y = x + 2
        x = n - 1
    if x < 0:
        x = y
        y = 0

    if arr[x][y]:
        dia_idx = n - 1 - (x - y)
        if not diagonal[dia_idx]:
            diagonal[dia_idx] = 1
            bishop[x][y] = 1
            if x + y >= n - 1:
                dfs(n - 1, x + y - (n - 1) + 1, cnt + 1)
            else:
                dfs(x + y + 1, 0, cnt + 1)
            diagonal[dia_idx] = 0
            bishop[x][y] = 0
    dfs(x - 1, y + 1, cnt)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bishop = [[0] * n for _ in range(n)]
diagonal = [0] * (n * 2 - 1)
max_val = float('-inf')

dfs(0, 0)
print(max_val)
