import sys

sys.stdin = open('input.txt')

n = int(input())
numbers = list(map(int, input().split()))

if n == 1:
    answer = 1
else:
    cnt1 = 1
    cnt2 = 1
    cnt1_max = 0
    cnt2_max = 0

    for i in range(n - 1):
        if numbers[i] <= numbers[i + 1]:
            cnt1 += 1
        else:
            cnt1 = 1

        if numbers[i] >= numbers[i + 1]:
            cnt2 += 1
        else:
            cnt2 = 1

        if cnt1_max < cnt1:
            cnt1_max = cnt1

        if cnt2_max < cnt2:
            cnt2_max = cnt2

    answer = max(cnt1_max, cnt2_max)

print(answer)
