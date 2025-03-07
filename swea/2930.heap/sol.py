import sys
sys.stdin = open('input.txt','r')

################################
def append(idx):
    if idx % 2:  #홀수면 부모의 오른쪽 자식
        parent = (idx - 1) // 2  # 부모노드
    else:
        parent = idx // 2    #부모노드
    if parent == 0:    #heap[0]을 더미 0번으로 해서    #부모루트가 없을때
        return

    if heap[parent] < heap[idx]:    #값이 크면 바꾸기
        heap[parent], heap[idx] = heap[idx], heap[parent]
    else:   #같거나 작으면 리턴
        return
    append(parent)

def dfs_delete(idx):
    if len(heap)-1 < (idx * 2):  #자식이 없으면
        return  #리턴

    if len(heap)-1 >= (idx * 2) + 1:   #오른쪽 자식이 있으면
        if heap[(idx * 2)] < heap[(idx * 2) + 1]:   #오른쪽이 더 크면 오른쪽에 삽입
            heap[idx], heap[(idx * 2) + 1] = heap[(idx * 2) + 1], heap[idx]
            dfs_delete((idx * 2) + 1)
            return

    heap[idx], heap[idx * 2] = heap[idx * 2], heap[idx]     #오른쪽 자식이 없거나 왼쪽 자식만 있으면
    dfs_delete(idx * 2)

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    heap = [0]  # 더미값
    ans = []

    for i in range(n):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            heap.append(arr[1])     # arr[1] 삽입 후
            idx = len(heap) - 1
            while True:
                if idx % 2:  # 홀수면 부모의 오른쪽 자식
                    parent = (idx - 1) // 2  # 부모노드
                else:
                    parent = idx // 2  # 부모노드
                if parent <= 0:  # heap[0]을 더미 0번으로 해서    #부모루트가 없을때
                    break
                if heap[parent] < heap[idx]:  # 값이 크면 바꾸기
                    heap[parent], heap[idx] = heap[idx], heap[parent]
                    idx = parent
                else:  # 같거나 작으면 리턴
                    break

        elif arr[0] == 2:
            # 최댓값 출력 후 키값 삭제
            if len(heap) - 1 == 0:
                ans.append(-1)
            else:
                ans.append(heap[1])
                heap[1] = heap[-1]
                heap.pop()
                idx = 1
                while True:
                    if len(heap) - 1 < (idx * 2):  # 왼쪽 자식이 없으면
                        break  # 리턴
                    if len(heap) - 1 >= (idx * 2) + 1:  # 오른쪽 자식이 있으면
                        if heap[(idx * 2)] < heap[(idx * 2) + 1] and heap[idx] <= heap[(idx * 2) + 1]:  # 왼쪽보다 오른쪽이 크고 자식이 더 크면
                            heap[idx], heap[(idx * 2) + 1] = heap[(idx * 2) + 1], heap[idx]
                            idx = idx * 2 + 1
                            continue
                    if heap[idx] < heap[idx * 2]:   # 왼쪽 자식이 더 크면
                        heap[idx], heap[idx * 2] = heap[idx * 2], heap[idx]  # 오른쪽 자식이 없거나 왼쪽 자식만 있으면
                        idx = idx * 2
                        continue
                    break
    print(f'#{tc}', end=" ")
    for i in ans:
        print(i, end=" ")
    print()
