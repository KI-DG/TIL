import sys

sys.stdin = open('input.txt')


def bfs():
    pass


for tc in range(1, 2):
    num, start = map(int, input().split())

    data = list(map(int, input().split()))

    graph = [[] for _ in range(101)]  # 인접 리스트를 만든다.

    for i in range(0, num//2):
        if graph[data[i * 2]] != data[i * 2 + 1]:
            graph[data[i * 2]].append(data[i * 2 + 1])

    bfs()
