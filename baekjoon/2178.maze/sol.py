from collections import deque
n, m = map(int, input().split())

arr = [list(map(int,input())) for _ in range(n)]
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def bfs(x=0, y=0):
    cnt = 1
    queue = deque([[x, y, cnt]])
    arr[x][y] = 0
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if nx == n - 1 and ny == m - 1:
                return cnt+1
            if arr[nx][ny]:
                queue.append([nx, ny, cnt+1])
                arr[nx][ny] = 0

print(bfs())
