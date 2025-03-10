def back(idx=0, cnt=0):
    if idx >= n-1:
        global max_val
        max_val = max(max_val, cnt)
        return
    if arr[idx][0] <= 0:
        idx += 1
        if idx >= n-1:
            return


    for i in range(n):
        if idx == i:
            continue
        if arr[i][0] <= 0:
            continue
        arr[idx][0] -= arr[i][1]
        arr[i][0] -= arr[idx][1]
        if arr[idx][0] <= 0 and arr[i][0] <= 0:
            back(idx + 1, cnt + 2)
        elif arr[idx][0] <= 0 or arr[i][0] <= 0:
            back(idx + 1, cnt + 1)
        else:
            back(idx + 1, cnt)

        arr[idx][0] += arr[i][1]
        arr[i][0] += arr[idx][1]
        back(idx + 1, cnt)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
max_val = float('-inf')

back()

print(max_val)