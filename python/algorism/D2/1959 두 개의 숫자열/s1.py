import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    a1 = list(map(int, input().split()))
    b1 = list(map(int, input().split()))

    if n < m:
        n, m = m, n
        a1, b1 = b1, a1

    answer = -99999999
    for i in range(n - m + 1):
        result = 0
        for j in range(m):
            result += a1[i + j] * b1[j]

        if answer < result:
            answer = result

    print(f'#{tc} {answer}')