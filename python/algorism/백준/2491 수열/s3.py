import sys

sys.stdin = open('input.txt')

n = int(input())
numbers = list(map(int, input().split()))


if n == 1:
    answer = 1
else:
    cnt1 = 1
    cnt2 = 1
    max_cnt1 = 0
    max_cnt2 = 0
    for i in range(n - 1):
        if numbers[i] <= numbers[i + 1]:
            cnt1 += 1
            if max_cnt1 < cnt1:
                max_cnt1 = cnt1
        else:
            cnt1 = 1

    for j in range(n - 1, 0, -1):
        if numbers[j] <= numbers[j - 1]:
            cnt2 += 1
            if max_cnt2 < cnt2:
                max_cnt2 = cnt2
        else:
            cnt2 = 1
    answer = max(max_cnt2, max_cnt1)
print(answer)
