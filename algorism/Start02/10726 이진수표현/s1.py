import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    answer = ''
    on_off = 'OFF'
    # m을 이진수로 변환
    while True:
        x = m % 2
        # 이진수를 뒤에서부터 저장
        answer += str(x)
        m = m // 2
        if m == 1:
            answer += str(m)
            break
        elif m == 0:
            break
    result = 0
    for i in range(n):
        if len(answer) < n:
            on_off = 'OFF'
        else:
            result += int(answer[i])

    if result == 1 * n:
        on_off = 'ON'

    print(f'#{tc} {on_off}')