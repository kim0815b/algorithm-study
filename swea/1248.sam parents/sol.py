import sys
sys.stdin = open('input.txt','r')

#################################
def dfs(node = 1):
    if node == num_1:
        return True
    if node == 0:
        return False

    boolean = dfs(left_child[node]) or dfs(right_child[node])
    if boolean:
        one_parents[node] = True
    return boolean


def right_dfs(node=1):
    if node == num_2:
        return True
    if node == 0:
        return False

    boolean = dfs(left_child[node]) or dfs(right_child[node])
    if boolean:
        two_parents[node] = True
    return boolean

def cnt_dfs():
    pass

T = int(input())
for tc in range(1, T+1):
    v, e, num_1, num_2 = map(int, input().split())

    left_child = [0] * (v+1)
    right_child = [0] * (v+1)

    one_parents = [False] * (v+1)
    two_parents = [False] * (v+1)

    arr = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        if left_child[arr[i]]:  # 왼쪽에 값이 있으면
            right_child[arr[i]] = arr[i + 1]  #오른쪽
        else:
            left_child[arr[i]] = arr[i + 1]   #왼쪽


    dfs()
    right_dfs()
    print(one_parents)
    print(two_parents)
    num = 0
    for i in range(v):
        if one_parents[i] and two_parents[i]:
            num = i
    print(num)
