import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())  # m초마다 k개씩 만들수 있다
    times = list(map(int, input().split()))
    times.sort()
    answer = 'Possible'

    total = 0  # 붕어빵의 개수

    # for i in range(n):
    #     if (times[i] // m) * k < i + 1:
    #         answer = 'Impossible'
    #         break

    for i in range(0, 11111 + 1):
        if t != 0 and t % m == 0:
            total += k

        if t in times:
            if total <= 0:
                answer = 'Impossible'
                break
            else:
                total -= 1

    print(f'#{tc} {answer}')