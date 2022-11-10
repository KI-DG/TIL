import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    num, danger = map(int, input().split())
    persons = list(map(int, input().split()))

    n = len(persons)  # 원소의 개수
    sum_list = []

    for i in range(1, 1 << n):  # 부분집합의 개수
        sum_value = 0  # 부분집합의 합
        for j in range(n):
            if i & (1 << j):
                sum_value += persons[j]
        if sum_value >= danger:      # 부분집합의 합에서 위험 높이 보다 큰 수를 추출
            sum_list.append(sum_value)      # 그 수를 리스트에 넣어준다

    min_sum_list = min(sum_list)   # 제일 작은 수를 찾아주고
    answer = min_sum_list - danger   # 그 값에서 위험 높이와 빼준다
    print(f'#{tc} {answer}')