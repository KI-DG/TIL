import sys

sys.stdin = open('input')


def powerset(depth, total):
    global minimum
    if minimum <= total:
        return

    if depth == n:
        if minimum > total:
            minimum = total
            return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                powerset(depth + 1, total + numbers[depth][i])
                visited[i] = False


t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    numbers = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    minimum = 100*15

    powerset(0, 0)
    print(f"#{tc} {minimum}")
