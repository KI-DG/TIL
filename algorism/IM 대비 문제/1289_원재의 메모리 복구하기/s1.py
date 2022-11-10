import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n = list(input())
    cnt = 0
    reset = ['0'] * len(n)
    # 돌면서 1이 나오면 그 다음부터 1이 아닌 숫자를 카운트 해라
    for i in range(len(n)):
        if n[i] != reset[i]:  # 1이 나오면
            for j in range(i, len(n)):
                reset[j] = n[i]
            cnt += 1

    print(f'#{tc} {cnt}')