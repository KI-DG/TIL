import sys

sys.stdin = open('input.txt')


def dfs(cnt, num, sum_num):
    global answer
    # 가지치기 (중간에 sum_num 값이 더 크면 빠져나와라)
    if answer <= sum_num:
        return
    # n회차이면 마지막 사무실에 돌아와야 한다
    if cnt == n:
        sum_num += arr[num][0]    # 마지막 사무실에 돌아오는 소모량 더해주고
        if answer > sum_num:      # 값이 더 작으면 갱신해주고
            answer = sum_num
        return

    for j in range(1, n):
        if arr[num][j] != 0 and not v[j]:           # 0의 값이 아니거나 방문하지 않았다면
            v[j] = 1                                # 방문체크를 해주고
            dfs(cnt + 1, j, sum_num + arr[num][j])  # 재귀로 다시 돌려주고
            v[j] = 0                                # 방문을 체크 취소


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    answer = 100 * n

    dfs(1, 0, 0)
    print(f'#{tc} {answer}')