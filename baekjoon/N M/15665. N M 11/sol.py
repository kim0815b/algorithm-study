def dfs(arr, M, path=[]):
    if len(path) == M:
        perms.append(path[:])
        return

    for i in range(len(arr)):
        path.append(arr[i])
        dfs(arr[i:], M, path)
        path.pop()

N, M = map(int, input().split())

arr = map(int, input().split())
perms = []
dfs(sorted(arr), M)

perms = set(map(tuple, perms))

for perm in sorted(perms):
    print(' '.join(map(str, perm)))