import sys

sys.stdin = open('input.txt')

# 시간 복잡도에서 아웃
# t = int(input())
#
# for tc in range(1, t + 1):
#     n = int(input())
#     measure_list = []
#     for i in range(1, int(n**(1/2)) + 1):
#         if n % i == 0:
#             measure_list.append(i)
#             if (i ** 2) != n:
#                 measure_list.append(n//i)
#     answer = -1
#     for j in measure_list:
#         if j*j*j == n:
#             answer = j
#
#
#     print(f'#{tc} {answer}')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = -1
    a = round(pow(n, (1/3)), 2)
    if a != int(a):
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {int(a)}')