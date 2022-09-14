# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last  # 자식
    p = c // 2   # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:  # 부모가 있고, 부모 < 자식 인 경우 자리교환 (부모가 없거나 부모 > 자식 조건을 만족할 때까지)
        heap[p], heap[c] = heap[c], heap[p]  # 자리를 바꿔준다
        c = p
        p = c // 2



heap = [0] * 100
last = 0
enq(2)
enq(5)
print()