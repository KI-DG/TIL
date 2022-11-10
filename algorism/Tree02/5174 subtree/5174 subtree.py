import sys

sys.stdin = open('input.txt')


def preorder(num):
    global cnt
    if num:
        cnt += 1
        preorder(ch1[num])
        preorder(ch2[num])


t = int(input())

for tc in range(1, t + 1):
    e, n = map(int, input().split())  # 간선의 개수 와 시작위치
    v = e + 1                         # 정점의 개수
    ch1 = [0] * (v + 1)               # 자식 1의 리스트
    ch2 = [0] * (v + 1)               # 자식 2의 리스트
    arr = list(map(int, input().split()))  # 배열을 받는다
    cnt = 0

    for i in range(e):
        parent, child = arr[i * 2], arr[i * 2 + 1]      # 부모 노드와 자식 노드를 가진다

        if ch1[parent] == 0:            # 부모 노드가 0이면 자식1에
            ch1[parent] = child
        else:                           # 0이 아니면 자식2에
            ch2[parent] = child
    preorder(n)
    print(f'#{tc} {cnt}')