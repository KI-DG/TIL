import sys

sys.stdin = open('input')


def dfs(idx):
    global answer, result

    if len(data) <= idx:  # 정류장에 도착하거나 넘어가면 결과값을 최소값으로 바꾸고 리턴
        if result >= answer:
            result = answer
        return
    if result <= answer:  # 가지치기 (최소값을 넘으면)
        result

    for i in range(idx + data[idx], idx, -1):
        answer += 1
        dfs(i)
        answer -= 1


t = int(input())

for tc in range(1, t + 1):
    data = list(map(int, input().split()))
    n = data[0]  # 버스 정류장 수
    result = 100000000
    answer = 0
    dfs(1)

    print(f'#{tc} {result -1}')