def dfs(N, M, path=[]):
    if len(path) == M:
        print(*path)
        return
    start = path[-1] if len(path) > 0 else 1
    for i in range(start, N+1):
        path.append(i)
        dfs(N, M, path)
        path.pop()

N, M = map(int, input().split())

dfs(N, M)

perms = []
