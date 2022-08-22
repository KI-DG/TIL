import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # n == 카드의 수
    card = list(map(str, input().split()))

    result = []

    for i in range(n):
        if n % 2:
            if i % 2:
                result.append(card[-1 * (n // 2) + (i // 2)])
            else:
                result.append(card[i // 2])
        else:
            if i % 2:
                result.append(card[(i // 2) + (n // 2)])
                # 홀수 인덱스
            else:
                result.append(card[i // 2])
                # 짝수 인덱스
    print(f'#{tc}', *result)