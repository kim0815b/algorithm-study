from collections import deque

def dfs(path=[],idx = 0):
    global ans
    if len(path) == 7 and bfs(path):
        ans += 1
        return
    if idx == 25:
        return
    path.append((idx // 5, idx % 5))
    dfs(path, idx + 1)
    path.pop()
    dfs(path, idx + 1)

def bfs(path):
    y_cnt = 0
    x, y = path[0]
    if arr[x][y] == 'Y':
        y_cnt += 1
    queue = deque([path[0]])
    visited = set([path[0]])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if (nx, ny) in path and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if arr[nx][ny] == 'Y':
                    y_cnt += 1
    if y_cnt > 3 or len(visited) != len(path):
        return False
    return True

arr = [input() for _ in range(5)]
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
ans = 0
dfs()
print(ans)