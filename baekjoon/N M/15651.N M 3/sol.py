# def dfs(arr, m):
#     if m == 1:
#         return [[x] for x in arr]
#
#     result = []
#     for i in range(len(arr)):
#         for j in dfs(arr, m-1):
#             perm = [arr[i]] + j
#             result.append(perm)
#             if m == M:
#                 print(' '.join(map(str, perm)))
#                 result.pop()
#     return result
#
# N, M = map(int, input().split())
#
# dfs(range(1,N+1), M)
# #

def dfs(N, m, path=[]):
    if len(path) == m:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        dfs(N, m, path)
        path.pop()

N, M = map(int, input().split())
permutation = []
dfs(N, M)

