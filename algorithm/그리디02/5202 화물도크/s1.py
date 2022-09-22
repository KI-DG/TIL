import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    time_schedule = [0] * 25
    date = [list(map(int, input().split()))for _ in range(n)]

    cnt = 0

    print(f'#{tc} {cnt}')