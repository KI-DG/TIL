import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    data = input()

    answer = ''
    for i in data:
        answer += i
        length = len(answer)
        if answer == data[length:length+length]:
            break

    print(f'#{tc} {len(answer)}')