import sys

sys.stdin = open('input.txt')


def bfs(v):
    visited = [False] * (n + 1)
    visited[v] = True
    queue = [v]

    while queue:
        v = queue.pop(0)
        answer.append(v)
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)


n = 7
bfs_list = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
answer =[]
for i in range(len(bfs_list)//2):
    s, e = bfs_list[i * 2], bfs_list[i * 2 + 1]
    graph[s].append(e)
    graph[e].append(s)

bfs(1)
print(*answer)
