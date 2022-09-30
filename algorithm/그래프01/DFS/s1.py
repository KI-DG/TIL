import sys

sys.stdin = open('input.txt')


def dfs(v):
    visited = [False] * (n + 1)
    visited[v] = True
    stack = [v]

    while stack:
        v = stack.pop()
        answer.append(v)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                stack.append(next_v)


n = 7
dfs_list = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]  # 인접리스트
answer = []

for i in range(len(dfs_list) // 2):
    s, e = dfs_list[i * 2], dfs_list[(i * 2) + 1]
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(*answer)
