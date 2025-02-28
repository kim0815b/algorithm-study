import sys
sys.stdin = open("input.txt","r")
#######################

def dfs(arr, path=[]):
    if len(path) == N:
        perms.append(path[:])
        return

    for i in range(len(arr)):
        path.append(arr[i])
        dfs(arr[:i] + arr[i+1:], path)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    arr = list(range(1,N+1))
    perms = []
    dfs(arr)

    for perm in perms:
        print(perm)