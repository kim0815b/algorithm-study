from collections import deque
def bfs(x, y):
    global max_val
    queue = deque([[x, y]])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if arr[nx][ny]:
                queue.append([nx, ny])
                arr[nx][ny] = 0
                cnt += 1
    max_val = max(max_val, cnt)

n, m = map(int, input().split())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
arr = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
pic_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            pic_cnt += 1
            arr[i][j] = 0
            bfs(i, j)
print(pic_cnt)
print(max_val)