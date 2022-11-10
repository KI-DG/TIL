import sys

sys.stdin = open('input.txt')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])     # 경로 압축을 해준다
    return parent[node]


n = int(input())    # 컴퓨터의 수
m = int(input())    # 연결할 수 있는 선의 수

network = []   # 다시 정렬하기 위해 빈 리스트 만들어 준다

for i in range(m):
    start, end, cost = map(int, input().split())
    network.append((cost, start, end))

network.sort()    # 비용의 기준으로 오름차순 정렬

parent = list(range(n + 1))     # make_set
counts, costs = 0, 0   # 간선의 개수, 총 비용의 합을 구하는 변수 생성

for w, s, e in network:         # find_set
    x_root = find_set(s)
    y_root = find_set(e)

    if x_root != y_root:        # union
        parent[y_root] = x_root
        costs += w
        counts += 1

        if counts >= n - 1:     # 최소 간선 수만 찾아주면 된다(최소 간선의 수 == 컴퓨터의수 -1)(가지치기)
            break

print(costs)
