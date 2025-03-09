def dfs(r=0, c=0, cnt=0):
    global max_val

    if r > len(rhombus) - 1:
        if max_val < cnt:
            max_val = cnt
        return

    if c > len(rhombus[r]) - 1:
        return

    if not diagonal[rhombus[r][c]]:
        diagonal[rhombus[r][c]] = 1
        dfs(r + 1, 0, cnt + 1)
        diagonal[rhombus[r][c]] = 0
    dfs(r, c + 1, cnt)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bishop = [[0] * n for _ in range(n)]
diagonal = [0] * (n * 2 - 1)
rhombus = [[] for _ in range(n * 2 - 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            rhombus[i+j].append(n - 1 - (i - j))
max_val = float('-inf')
rhombus = [i for i in rhombus if i]

for i in rhombus:
    print(i)

dfs()
print(max_val)
