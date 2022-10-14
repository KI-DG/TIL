import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(n)])

    cnt = [0] * 201
    for room in arr:
        if room[0] < room[1]:
            start = (room[0] + 1) // 2
            end = (room[1] + 1) // 2
        else:
            end = (room[0] + 1) // 2
            start = (room[1] + 1) // 2

        for j in range(start, end + 1):
            cnt[j] += 1

    ans = max(cnt)

    print(f'#{tc} {ans}')
