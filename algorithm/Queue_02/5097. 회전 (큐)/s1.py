import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(m):
        queue.append(queue.pop(0))

    print(f'#{tc} {queue.pop(0)}')