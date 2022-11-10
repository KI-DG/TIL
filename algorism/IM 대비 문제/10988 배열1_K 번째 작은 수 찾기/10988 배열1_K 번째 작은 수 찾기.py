import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count_arr = [0] * 1001
    for i in arr:
        count_arr[i] = i

    cnt = 0
    answer = []
    for i in range(n):
        if count_arr[i] != 0:
            cnt += 1
            if cnt == k:
                answer.append(count_arr[i])

    print(f'#{tc}', *answer)