import sys

sys.stdin = open('input.txt')


# calculator ={
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y,
# }


def in_order(node):

    if node:
        in_order(ch1[node])
        in_order(ch2[node])
        if tree[node] == '-':
            tree[node] = str(int(tree[ch1[node]]) - int(tree[ch2[node]]))
        elif tree[node] == '+':
            tree[node] = str(int(tree[ch1[node]]) + int(tree[ch2[node]]))
        elif tree[node] == '*':
            tree[node] = str(int(tree[ch1[node]]) * int(tree[ch2[node]]))
        elif tree[node] == '/':
            tree[node] = str(int(tree[ch1[node]]) / int(tree[ch2[node]]))


t = 10

for tc in range(1, t + 1):
    n = int(input())
    tree = [''] * (n + 1)
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    for i in range(n):
        data = input().split()
        if len(data) == 2:
            tree[int(data[0])] = int(data[1])
        else:
            tree[int(data[0])] = data[1]
            ch1[int(data[0])] = int(data[2])
            ch2[int(data[0])] = int(data[3])

    in_order(1)

    print(f'#{tc} {tree[1]}')