import sys

sys.stdin = open('input.txt')


def in_order(num):
    global cnt
    if num <= n:
        in_order(num * 2)
        arr[num] = cnt
        cnt += 1
        in_order(num * 2 + 1)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [0] * (n + 1)
    cnt = 1
    in_order(1)
    print(f'#{tc} {arr[1]} {arr[n//2]}')
