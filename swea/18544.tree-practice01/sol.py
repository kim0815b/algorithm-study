import sys
sys.stdin = open('input.txt','r')

#################################
def dfs(node):
    print(node, end=" ")
    if node not in tree.keys():
        return
    if not len(tree[node]):
        return
    for i in tree[node]:
        dfs(i)

T = 1
for tc in range(1, T+1):
    v = int(input())
    arr = list(map(int, input().split()))
    tree = {}

    for i in range(0, len(arr), 2):
        if not tree.setdefault(arr[i], False):
            tree[arr[i]] = []
        tree[arr[i]].append(arr[i + 1])

    dfs(arr[0])