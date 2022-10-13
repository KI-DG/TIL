# 1. 왼쪽부터 시작하여 기둥이 나오면 그 기둥부터 다음 큰 기둥까지 범위내의 값을 높이만큼 더해준다
# 2. 제일 큰 기둥이 나오기 전까지 반복
# 3. 젤 큰 기둥이 나오면 오른쪽부터 반복
# 4. 제일 큰 기둥이 나오기 전까지 반복

import sys

sys.stdin = open('input.txt')

n = int(input())

storage = []                                     # 빈 리스트 생성
storage_list = [0] * 1001                        # 배열생성
for i in range(n):                               # 왼쪽으로부터 면의 위치와 높이
    left, height = map(int, input().split())
    storage.append([left, height])

storage.sort()                                   # 리스트 정렬을 해준다
right_max = 0                                    # 제일 오른쪽에 위치한 곳을 지정할 변수
height_max = 0                                   # 가장 큰 높이를 저장할 변수
height_index = 0                                 # 가장 큰 높이의 인덱스를 저장할 변수
for x, y in storage:
    storage_list[x] = y                          # 높이 저장
    right_max = x                                # 가장 오른쪽에 위치한 곳 저장
    if y > height_max:                           # 가장 큰 높이와 인덱스를 찾음
        height_max = y
        height_index = x

answer = 0                                       # 저장할 값 생성
answer += height_max
for j in range(height_index):                           # 가장 큰 높이까지
    a = 1
    if storage_list[j] > storage_list[j - 1]:
        while True:
            a += 1
            if storage_list[j] <= storage_list[j + a]:
                answer += storage_list[j] * a
                break
        if j + a == height_index:
            break
for k in range(right_max, height_index, -1):            # 오른쪽에서 큰 높이까지
    b = 1
    if storage_list[k] > storage_list[k - 1]:
        while True:
            b += 1
            if storage_list[k] <= storage_list[k - b]:
                answer += storage_list[k] * b
                break
        if k - b == height_index:
            break

print(answer)

