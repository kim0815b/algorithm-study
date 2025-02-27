def dfs(arr, M, path = []):
    if len(path) == M:
        print(*path)
        return

    for i in range(len(arr)):
        path.append(arr[i])
        dfs(arr, M, path)
        path.pop()

N, M = map(int, input().split())

arr = sorted(map(int, input().split()))

dfs(arr, M)

