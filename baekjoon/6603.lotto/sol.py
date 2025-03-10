def dfs(path=[], idx=0):
    if len(path) == 6:
        print(*path)
        return
    if idx == len(arr):
        return
    path.append(arr[idx])
    dfs(path, idx + 1)
    path.pop()
    dfs(path, idx + 1)

while True:
    inp = input()
    if inp == '0':
        break
    inp = inp[2:]
    arr = list(map(int, inp.split()))
    arr.sort()
    dfs()
    print()