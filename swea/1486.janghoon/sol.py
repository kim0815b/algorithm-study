import sys

sys.stdin = open("input.txt", "r")
#

#######################
def dfs(idx, sum):
    global ans

    if ans <= sum-B:
        return

    if idx == N:
        if sum >= B:
            ans = min(ans, sum-B)
        return
    dfs(idx + 1, sum + arr[idx])
    dfs(idx + 1, sum)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = float('inf')
    dfs(0, 0)

    print(f'#{tc} {ans}')
