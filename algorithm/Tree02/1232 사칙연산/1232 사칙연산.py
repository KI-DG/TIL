import sys

sys.stdin = open('input.txt')


def in_order(node):
    global answer
    if node <= n:
        in_order(node * 2)
        answer.append(tree[node])
        in_order(node * 2 + 1)


t = 10

for tc in range(1, t + 1):
    n = int(input())
    tree = [''] * (n + 1)
    answer = []
    for i in range(n):
        data = list(input().split())
        if len(data) == 2:
            tree[int(data[0])] = int(data[1])
        else:
            tree[int(data[0])] = data[1]

    in_order(1)
    print(answer)
