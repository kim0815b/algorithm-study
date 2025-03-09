def dfs_odd(x, y, cnt=0):
    global max_val_01

    if x + y >= 2 * n - 3 and y > n - 1:
        if max_val_01 < cnt:
            max_val_01 = cnt
        return

    if y > n - 1:
        y = x + 3
        x = n - 1
    if x < 0:
        x = y + 1
        y = 0

    if arr[x][y]:
        dia_idx = n - 1 - (x - y)
        if not diagonal[dia_idx]:
            diagonal[dia_idx] = 1
            if x + y + 2 > n - 1:
                dfs_odd(n - 1, x + y - (n - 1) + 2, cnt + 1)
            else:
                dfs_odd(x + y + 2, 0, cnt + 1)
            diagonal[dia_idx] = 0
    dfs_odd(x - 1, y + 1, cnt)

def dfs_even(x, y, cnt=0):
    global max_val_01

    if x + y >= 2 * n - 3 and y > n - 1:
        if max_val_01 < cnt:
            max_val_01 = cnt
        return

    if y > n - 1:
        if x < 0:
            y = x + 2
        else:
            y = x + 3
        x = n - 1
    if x < 0:
        if y >= n - 1:
            y = x + 2
            x = n - 1
        else:
            x = y + 1
            y = 0

    if arr[x][y]:
        dia_idx = n - 1 - (x - y)
        if not diagonal[dia_idx]:
            diagonal[dia_idx] = 1
            if x + y + 2 > n - 1:
                dfs_even(n - 1, x + y - (n - 1) + 2, cnt + 1)
            else:
                dfs_even(x + y + 2, 0, cnt + 1)
            diagonal[dia_idx] = 0
    dfs_even(x - 1, y + 1, cnt)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bishop = [[0] * n for _ in range(n)]
diagonal = [0] * (n * 2 - 1)

max_val_01 = 0
if n % 2 == 1:
    dfs_odd(0, 0)
    cnt = max_val_01
    max_val_01 = 0
    dfs_even(1, 0)
    cnt += max_val_01
else:
    dfs_even(0, 0)
    cnt = max_val_01
    max_val_01 = 0
    dfs_odd(1, 0)
    cnt += max_val_01

print(cnt)
