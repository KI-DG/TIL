import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]

    color = []

    for i in range(1, n - 1):
        for j in range(1 + i, n):
            w = arr[0:i]
            b = arr[i:j]
            r = arr[j:n]
            w_count = 0
            for k in range(i):
                for d in range(m):
                    if w[k][d] == 'W':
                        w_count += 1
            for k in range(j - i):
                for d in range(m):
                    if b[k][d] == 'B':
                        w_count += 1
            for k in range(n - j):
                for d in range(m):
                    if r[k][d] == 'R':
                        w_count += 1
            color.append(w_count)
    answer = n * m - max(color)

    print(f'#{tc} {answer}')


