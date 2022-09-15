import sys

sys.stdin = open('input.txt')


# def heap_push(item):
#     heap.append(item)
#     child = len(heap) - 1
#     parent = child // 2
#
#     while parent > 0 and heap[parent] > heap[child]:
#         heap[parent], heap[child] = heap[child], heap[parent]
#         child = parent
#         parent = child // 2
#

t = int(input())

for tc in range(1, t + 1):
    n = int(input())                            # 노드의 개수
    arr = list(map(int, input().split()))       # 트리를 만들 배열을 가져옴

    heap = [0]                                  # 완전 이진 트리를 위한 리스트를 만들어줌 index를 맞추기 위해 0을 삽입
    for i in range(len(arr)):
        heap.append(arr[i])                     # 반복문을 통해 삽입을 해주고
        child = len(heap) - 1
        parent = child // 2

        while parent > 0 and heap[parent] > heap[child]:            # 최소힙 트리를 만들어 주기 위해 반복문을 써준다
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            parent = child // 2

    answer = 0
    for j in range(len(heap), 0, -1):           # 조상로드의 값을 더해줘야 하기 때문에 반복문을 써준다
        if j == n // 2:
            answer += heap[j]
            n = n // 2
    print(f'#{tc} {answer}')