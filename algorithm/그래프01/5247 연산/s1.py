import sys
from collections import deque
sys.stdin = open('input.txt')

cal = [
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: x * 2,
    lambda x: x - 10,
]
# 람다 함수로 계산기를 만들어준다


def bfs(x):                  # 다시 뒤로 돌아가고 같은 라인에 있을때 카운트를 해주기 위해 bfs를 사용해준다
    visited = set()          # 중복으로 방문하지 않기 위해 set을 해준다
    queue = deque([[n, 0]])  # 시간초과가 나지 않도록 deque를 이용해준다
    visited.add(n)           # 방문한 기록을 남겨준다

    while queue:
        v, cnt = queue.popleft()  # 왼쪽의 값과 cnt == 0으로 초기화해서 나와준다
        cnt += 1                  # 카운트를 해준다

        for i in range(4):        # 계산기가 4개 뿐이라 4번 반복
            cal_v = cal[i](v)
            if 1 <= cal_v <= 1000000 and cal_v not in visited:      # 가격의 값이 1보다 크고 1000000보다 작은 자연수 이며 방문하지 않아야 된다
                if cal_v == m:         # 값이 목표하는 값과 같으면 횟수를 찾는 거기 때문에 카운트를 리턴
                    return cnt
                visited.add(cal_v)     # 아니면 방문기록을 남긴다
                queue.append([cal_v, cnt])    # queue 에 더해준다(bfs하기 위해)


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    print(f'#{tc} {bfs(n)}')