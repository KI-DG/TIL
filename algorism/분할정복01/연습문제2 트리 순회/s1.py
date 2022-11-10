import sys

sys.stdin = open('input.txt')


def pre_order(n):
    if n:
        pre_order_list.append(n)
        pre_order(ch1[n])
        pre_order(ch2[n])


def in_order(n):
    if n:
        in_order(ch1[n])
        in_order_list.append(n)
        in_order(ch2[n])


def post_order(n):
    if n:
        post_order(ch1[n])
        post_order(ch2[n])
        post_order_list.append(n)


for tc in range(1):
    v, w = map(int, input().split())
    arr = list(map(int, input().split()))

    ch1 = [0] * (v + 1)
    ch2 = [0] * (v + 1)

    for i in range(w):
        p, c = arr[i * 2], arr[i * 2 + 1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    pre_order_list = []
    in_order_list = []
    post_order_list = []
    pre_order(1)
    in_order(1)
    post_order(1)

    print(f'전위 순회 :', *pre_order_list)
    print(f'중위 순회 :', *in_order_list)
    print(f'후위 순회 :', *post_order_list)
