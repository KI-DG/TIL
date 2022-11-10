import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))

    sum_min = 10000 * 100
    sum_max = 0

    for i in range(n -m +1):
        m_sum = 0
        for j in range(m):
            m_sum += ai[i+j]

        if sum_min > m_sum:
            sum_min = m_sum
        if sum_max < m_sum:
            sum_max = m_sum

    print(f'#{tc} {sum_max-sum_min}')

    # sliding window

