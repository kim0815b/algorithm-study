import sys
sys.setrecursionlimit(10**5)
n = int(input())

tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n-1):
    f, s = map(int, input().split())
    tree[f].append(s)
    tree[s].append(f)

def dfs(node=1):
    for i in tree[node]:
        if visited[i]:
            continue
        visited[i] = node
        dfs(i)
    return
visited[1] = 1
dfs(1)
for i in range(2, n+1):
    print(visited[i])