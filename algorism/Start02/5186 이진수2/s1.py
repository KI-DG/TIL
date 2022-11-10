import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = float(input())
    answer = ''

    while True:
        a = n * 2
        answer += str(int(a))
        n = a - int(a)
        if n == 0:
            break
        elif len(answer) > 12:
            answer = 'overflow'
            break

    print(f'#{tc} {answer}')

