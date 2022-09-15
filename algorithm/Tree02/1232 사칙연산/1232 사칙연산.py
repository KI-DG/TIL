import sys

sys.stdin = open('input.txt')


def in_order(node):
    global answer
    if node <= n:
        in_order(node * 2)
        if tree[node] == '+':
            answer += node
        elif tree[node] == '-':
            answer -= node
        # elif tree[node] == '*':
        #     answer *= node
        # else:
        #     answer /= node
        in_order(node * 2 + 1)


t = 1

for tc in range(1, t + 1):
    n = int(input())
    tree = [''] * (n + 1)
    answer = 0
    for i in range(n):
        data = list(input().split())
        if len(data) == 2:
            tree[int(data[0])] = int(data[1])
        else:
            tree[int(data[0])] = data[1]

    in_order(1)
    print(answer)
