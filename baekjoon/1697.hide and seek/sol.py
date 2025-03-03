from collections import deque


def bfs(n):
    queue = deque()
    queue.append((n, 0))

    while queue:                    # n ~   k   n < k <  (k-n) // 2  <  k < n * 2
        n, cnt = queue.popleft()
        if n == k:
            return cnt
        if n * 2 > k :
            queue.append((n - 1, cnt + 1))

        queue.append((n + 1, cnt + 1))
        if n:
            queue.append((n * 2, cnt + 1))


n, k = map(int, input().split())

print(bfs(n))
