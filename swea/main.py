def dfs(arr, m, path = []):
    if len(path) == m:
        print(*path)
        return
    for i in range(len(arr)):
        path.append(arr[i])
        dfs(arr[:i] + arr[i+1:], m, path)
        path.pop()

arr = list(range(1, 5))

dfs(arr, 4)

