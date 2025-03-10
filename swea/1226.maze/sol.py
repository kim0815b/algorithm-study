from collections import deque
import sys
sys.stdin = open('input.txt','r')

#################################
def bfs():
    queue = deque()
    queue.append((2, 2))
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > 15 or ny > 15:
                continue
            if arr[nx][ny] != 0:
                queue.append((nx, ny))





T = 10
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(16)]

    dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    ans = 0
    bfs()

    print(f'#{tc} {ans}')
