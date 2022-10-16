import sys

sys.stdin = open('input.txt')

n = int(input())
numbers = list(map(int, input().split()))

cnt = 1
max_cnt = 0
if n == 1:
    max_cnt = 1
else:
    for i in range(n - 1):
        if numbers[i] <= numbers[i + 1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    for j in range(n - 1, 0, -1):
        if numbers[j] <= numbers[j - 1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
print(max_cnt)
# 틀렸습니다
