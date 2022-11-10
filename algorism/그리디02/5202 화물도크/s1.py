import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    data = sorted([list(map(int, input().split()))for _ in range(n)], key=lambda x: x[1])

    # 시작조건
    i = 0
    j = 1

    cnt = 1

    while j < n:
        if data[i][1] <= data[j][0]:
            cnt += 1
            i = j
            j += 1

        else:
            j += 1

    print(f'#{tc} {cnt}')