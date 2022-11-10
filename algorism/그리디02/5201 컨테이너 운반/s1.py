import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    n_weights = sorted(list(map(int, input().split())), reverse=True)
    m_weights = sorted(list(map(int, input().split())), reverse=True)
    answer = 0

    for m_weight in m_weights:
        for n_weight in n_weights:
            if m_weight >= n_weight:
                answer += n_weight
                n_weights.remove(n_weight)
                break

    print(f'#{tc} {answer}')