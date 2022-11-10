import sys

sys.stdin = open('input')


def chk(number):
    number_string = str(number)
    for k in range(len(number_string) - 1):
        if number_string[k] > number_string[k+1]:
            return False
    return True


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            num = arr[i] * arr[j]
            if chk(num):
                answer = max(answer, num)

    print(f'#{tc} {answer}')
