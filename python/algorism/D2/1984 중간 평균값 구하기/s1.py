import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    data = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(1, 9):
        answer += data[i]

    result = round(answer/8)

    print(f'#{tc} {result}')

