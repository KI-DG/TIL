import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def find_set(node):
    if node != parents[node]:
        parents[node] = find_set(parents[node])
    return parents[node]


n, m = map(int, input().split())

sep = [[] for _ in range(n + 1)]
house_list = []
for i in range(m):
    s, e, w = map(int, input().split())
    sep[s].append((e, w))
    house_list.append((w, s, e))

house_list.sort()
parents = list(range(n + 1))

count, cost = 0, 0

for dist, x, y in house_list:
    x_root, y_root = find_set(x), find_set(y)

    if x_root != y_root:
        parents[y_root] = x_root
        cost += dist
        count += 1

        if count == n - 2:
            break

print(cost)


# 마을을 분리하고 - 마을안에서는 하나의 길만 존재 (X)
# 최소 비용을 구하고 마지막 제일 큰 길 하나만 제거