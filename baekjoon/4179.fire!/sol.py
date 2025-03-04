from collections import deque
r, c = map(int, input().split())

arr = [[i for i in input()] for _ in range(r)]

def bfs(jihun, fire):
    jihun_sec = deque()
    fire_sec = deque()
    while True:
        while jihun:
            jx, jy, cnt = jihun.popleft()
            if arr[jx][jy] == 'F':
                continue
            for dx, dy in dxy:
                x = dx + jx
                y = dy + jy
                if x < 0 or y < 0 or x > r-1 or y > c-1:
                    return cnt + 1
                if arr[x][y] == '#' or arr[x][y] == 'F' or arr[x][y] == 'J':
                    continue
                arr[x][y] = 'J'
                jihun_sec.append([x, y, cnt + 1])

        while fire:
            fx, fy = fire.popleft()
            for dx, dy in dxy:
                x = dx + fx
                y = dy + fy
                if x < 0 or y < 0 or x > r-1 or y > c-1 or arr[x][y] == '#' or arr[x][y] == 'F':
                    continue
                arr[x][y] = 'F'
                fire_sec.append([x, y])

        if not jihun_sec:
            return 0

        while jihun_sec:
            jihun.append(jihun_sec.popleft())
        while fire_sec:
            fire.append(fire_sec.popleft())



jihun = deque()
fire = deque()
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            jihun.append([i, j, 0])
        elif arr[i][j] == 'F':
            fire.append([i, j])

cnt = bfs(jihun, fire)
print(f'{cnt if cnt else "IMPOSSIBLE" }')