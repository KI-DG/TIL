'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

import sys

sys.stdin = open("input")


def preorder(n):  # 전위 순회
    # global cnt
    if n:
        # cnt += 1 길이를 나타날때
        # cnt = n  마지막 번호
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')


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
root = 1
# cnt = 0
preorder(3)
# print(cnt)
# inorder(root)
# print()
# postorder(root)
