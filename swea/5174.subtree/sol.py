import sys
sys.stdin = open('input.txt','r')

def dfs(root):
    global cnt
    if not len(node[root]):
        return

    for i in node[root]:
        dfs(i)
        cnt += 1

#################################
T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 1
    node = {}
    visited = [False] * (e+1)
    for i in range(1, e+2): # 노드 초기값
        node[i] = []
    for i in range(0, e * 2, 2):
        node[arr[i]].append(arr[i+1])

    dfs(n)
    print(f'#{tc} {cnt}')