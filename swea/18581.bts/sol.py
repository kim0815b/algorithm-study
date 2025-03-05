import sys
sys.stdin = open('input.txt','r')

#################################
def preorder_dfs(node):
    print(node, end=" ")
    if node not in tree.keys():
        return
    if not len(tree[node]):
        return
    for i in tree[node]:
        preorder_dfs(i)

def inorder_dfs(node):
    if node in tree.keys() and tree[node][0]:
        inorder_dfs(tree[node][0])
    print(node, end=" ")
    if node in tree.keys() and len(tree[node]) > 1 and tree[node][1]:
        inorder_dfs(tree[node][1])

def postorder_dfs(node):
    if node in tree.keys() and tree[node][0]:
        postorder_dfs(tree[node][0])
    if node in tree.keys() and len(tree[node]) > 1 and tree[node][1]:
        postorder_dfs(tree[node][1])
    print(node, end=" ")


T = 1
for tc in range(1, T+1):
    v = int(input())
    arr = list(map(int, input().split()))
    tree = {}

    for i in range(0, len(arr), 2):
        if not tree.setdefault(arr[i], False):
            tree[arr[i]] = []
        tree[arr[i]].append(arr[i + 1])

    print(tree)
    preorder_dfs(arr[0])
    print()
    inorder_dfs(arr[0])
    print()
    postorder_dfs(arr[0])

'''
            1
        2           3
        4       5       6
        7     8   9   10  11
        12                13

'''