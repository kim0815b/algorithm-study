def perm(arr, path, result):
    if not arr:
        result.append(path[:])  # 복사해서 저장
        return

    for i in range(len(arr)):
        path.append(arr[i])  # 현재 요소 추가
        perm(arr[:i] + arr[i + 1:], path, result)  # 재귀 호출
        path.pop()  # 원상복구 (백트래킹)

def comb(arr, r, path, index, result):
    if len(path) == r:
        result.append(path[:])  # 복사해서 저장
        return

    for i in range(index, len(arr)):
        path.append(arr[i])  # 현재 요소 추가
        comb(arr, r, path, i + 1, result)  # 재귀 호출

nums = [1, 2, 3]
result = []
comb(nums, 2, [], 0, result)
print(result)
