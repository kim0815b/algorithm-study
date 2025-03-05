import sys
sys.stdin = open('input.txt','r')

#################################
def dfs(num):
    if node[num]:
        return node[num]
    else:
        child_num = (num+1) * 2 - 1
        if child_num + 1 <= n - 1:
            sum_val = dfs(child_num) + dfs(child_num + 1)
        else:
            sum_val = dfs(child_num)
        node[num] = sum_val
        return sum_val

T = int(input())
for tc in range(1, T+1):

    n, m, l = map(int, input().split())
    node = [0] * n
    for _ in range(m):
        num, val = map(int, input().split())
        node[num - 1] = val
    dfs(0)
    print(f'#{tc} {node[l - 1]}')
