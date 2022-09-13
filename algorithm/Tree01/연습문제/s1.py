import sys

sys.stdin = open("input")


def preorder(n):  # 전위 순회
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


v = int(input())    # 정점 개수, 마지막 정점 번호
arr = list(map(int, input().split()))

e = v - 1  # 간선의 개수
ch1 = [0] * (v + 1)
ch2 = [0] * (v + 1)
for i in range(e):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c  # 자식 1에 저장
    else:
        ch2[p] = c  # 자식 2에 저장

preorder(1)