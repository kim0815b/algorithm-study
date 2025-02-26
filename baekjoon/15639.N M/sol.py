def dfs(arr, m):
    if m == 1:
        return [[x] for x in arr]
    result = []
    for i in range(len(arr)):
        for j in dfs(arr[:i] + arr[i+1:], m-1):
            result.append([arr[i]] + j)
    return result

N, M = map(int, input().split())

result = dfs(list(range(1, N + 1)), M)

for i in result:
    for j in i:
        print(j, end=" ")
    print()