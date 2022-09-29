import sys

sys.stdin = open('input.txt')


def find_set(node):
    if node != parents[node]:
        parents[node] = find_set(parents[node])
    return parents[node]


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    parents = list(range(n + 1))             # make_set

    for i in range(m):
        start, end = data[i*2], data[i*2 + 1]      # find_set
        start_root, end_root = find_set(start), find_set(end)

        if start_root < end_root:             # union
            parents[end_root] = start_root
        else:
            parents[start_root] = end_root

    answer = set()
    for i in range(1, n + 1):
        answer.add(find_set(i))

    print(f'#{tc} {len(answer)}')
