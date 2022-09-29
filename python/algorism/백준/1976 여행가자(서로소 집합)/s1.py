# 집합이면 된다
import sys

sys.stdin = open('input.txt')


def find_set(node):                     # find_set
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(x, y):                        # union 작은값에 저장
    x = find_set(x + 1)
    y = find_set(y + 1)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
m = int(input())
parent = list(range(n + 1))       # make_set

for i in range(n):
    city_map = list(map(int, input().split()))
    for j in range(1, n):           # find_set
        if city_map[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
result = 'YES'
root = find_set(plan[0])
for i in range(1, m):
    if root != find_set(plan[i]):
        result = 'NO'
print(result)
