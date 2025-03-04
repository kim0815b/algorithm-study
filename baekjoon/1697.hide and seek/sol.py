from collections import deque


def bfs(n):
    queue = deque()
    queue.append((n, 0))

    while queue:                    # n ~   k   n < k <  (k-n) // 2  <  k < n * 2
        n, cnt = queue.popleft()
        if n == k:
            return cnt
        if n-1 >= 0 and path[n - 1] == 0:
            path[n - 1] = 1
            queue.append((n - 1, cnt+1))
        if n * 2 <= 100000 and path[n * 2] == 0:
            path[n * 2] = 1
            queue.append((n * 2, cnt+1))
        if n + 1 <= 100000 and path[n + 1] == 0:
            path[n + 1] = 1
            queue.append((n + 1, cnt+1))

n, k = map(int, input().split())
path = [0] * 100001

print(bfs(n))
