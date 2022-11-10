import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    lst = list(map(int, input()))
    answer = []
    n = 0
    for i in range(len(lst)):
        n = lst[i] + n * 2
        if (i % 7) == 6:
            answer.append(n)
            n = 0

    print(f'#{tc}', *answer)
