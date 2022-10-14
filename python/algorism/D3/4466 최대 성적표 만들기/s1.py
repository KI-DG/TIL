import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    study = list(map(int, input().split()))

    study.sort(reverse=True)
    result = 0
    for i in range(k):
        result += study[i]

    print(f'#{tc} {result}')