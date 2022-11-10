def dfs(v):     # 재귀함수로 사용해야 편하다.
    global total
    visted[v] = True    # 방문했는지 체크, 방문했으면 True로 바꿔주고

    for next_v in graph[v]:
        if not visted[next_v]:
            total += 1
            dfs(next_v)


t = int(input())
n = int(input())
graph = [[] for _ in range(t + 1)]    # 0은 사용하지 않으므로 +1해준다. 1. 리스트를 만들어준다.
visted = [False] * (t + 1)  # [False]리스트를 만들어준다. 방문하지 않는 곳을 알아보기 위해
total = 0

for _ in range(n):  # 돌아가면서 리스트에 넣어준다
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(total)