import sys

sys.stdin = open('input.txt')


def find_set(node):
    if node != parents[node]:
        parents[node] = find_set(parents[node])
    return parents[node]


t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())
    costs = []                         # 정렬을 위해 빈리스트 생성
    parents = list(range(v + 1))       # make_set
    for _ in range(e):
        start, end, weigth = map(int, input().split())
        costs.append((weigth, start, end))    # 가중치가 제일 앞으로 오게끔 리스트에 넣어준다

    costs.sort()           # 가중치 기준으로 정렬
    counts, answer = 0, 0     # 간선의 개수와 정답을 출력하기 위해 초기값 설정

    for w, s, e in costs:            # find_set
        x_roots = find_set(s)
        y_roots = find_set(e)

        if x_roots != y_roots:           # union
            parents[y_roots] = x_roots
            answer += w                  # 가중치를 더해준다
            counts += 1                  # 간선 +1

            if counts >= v:              # 0이 포함되니까 -1은 안해준다
                break

    print(f'#{tc} {answer}')
