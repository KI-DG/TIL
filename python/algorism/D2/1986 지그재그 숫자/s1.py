import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    n_list = []
    answer = 0
    for i in range(1, n + 1):
        n_list.append(i)

    for num in n_list:
        if num % 2:
            answer += num
        else:
            answer -= num

    print(f'#{tc} {answer}')
