import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m, x = map(int, input().split())         # 노드의 개수, 리프 노드의 개수, 출력할 값

    ch1 = [0] * (n + 2)                         # 오른쪽 자식 노드가 없을 시에는 0
    for i in range(m):                          # 리프 노드의 값을 받아와 준다
        p, c = map(int, input().split())
        ch1[p] = c

    for i in range(n - m, 0, -1):               # 조상 노드의 값을 입력을 해준다
        ch1[i] = ch1[i * 2] + ch1[i * 2 + 1]

    answer = ch1[x]

    print(f'#{tc} {answer}')