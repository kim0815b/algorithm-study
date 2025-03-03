from collections import deque

def bfs(queue_01):
    queue_02 = deque()
    cnt = 0
    flag = False
    while True:
        while queue_01:
            x, y = queue_01.popleft()
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or arr[nx][ny] != 0:
                    continue
                arr[nx][ny] = 1
                queue_02.append([nx, ny])
                flag = True
        if flag:
            cnt += 1
        if not queue_02 or not flag:
            if [j for i in arr for j in i].count(0):
                return -1
            return cnt
        while queue_02:
            queue_01.append(queue_02.popleft())
        flag = False

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i,j])

print(bfs(queue))

