def dfs(arr, m, sel=[]):
    if m == 1:
        return [[x] for x in arr]
    result = []
    for i in range(len(arr)):
        sel.append(i)
        for j in dfs(arr[i+1:], m-1, sel):
            result.append([arr[i]] + j)
        sel.append(i)
    return result

N, M = map(int, input().split())

result = dfs(list(range(1, N + 1)), M)

for i in result:
    for j in i:
        print(j, end=" ")
    print()