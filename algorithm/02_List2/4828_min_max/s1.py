import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    numbers = input()
    ai = list(map(int, input().split()))

    for i in range(len(ai) - 1, 0, -1):
        for j in range(0, i):
            if ai[j] > ai[j + 1]:
                ai[j], ai[j + 1] = ai[j + 1], ai[j]

    max_min = ai[len(ai)-1] - ai[0]

    print(f'#{tc} {max_min}')






