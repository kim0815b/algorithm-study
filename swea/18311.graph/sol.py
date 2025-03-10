import sys
sys.stdin = open('input.txt','r')

def dfs(path=[], idx=1):
    if visited[idx]:
        return
    if not graph[idx]:
        return
    path.append(idx)
    visited[idx] = 1
    for i in graph[idx]:
        dfs(path, i)


#################################
T = 1
for tc in range(1, T+1):
    v, e = map(int, input().split())

    arr = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(0, e * 2, 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
    path = []
    dfs(path, 1)
    print(f'#{tc} {"-".join(map(str, path))}')

