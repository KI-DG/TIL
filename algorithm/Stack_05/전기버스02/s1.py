import sys

sys.stdin = open('input')


def permutation(arr):
    global total

    if len(arr) == n:
        print(arr)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(data[i])
        permutation(arr)

        visited[i] = False
        arr.pop()


t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    n = data[0]
    visited = [False] * n
    total = 0

    permutation([])

    print(f'#{tc} {a}')


