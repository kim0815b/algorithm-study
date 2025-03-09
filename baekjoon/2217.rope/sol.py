n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
max_val = float('-inf')

for i in range(len(arr)):
    w = arr[i] * (len(arr) - i)
    if max_val < w:
        max_val = w
print(max_val)