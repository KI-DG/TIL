import sys

sys.stdin = open('input.txt')

n = int(input())

storage = []                                     # 빈 리스트 생성
storage_list = [0] * 1001                        # 배열생성

for i in range(n):                               # 왼쪽으로부터 면의 위치와 높이
    left, height = map(int, input().split())
    storage.append([left, height])

storage.sort()                                   # 리스트 정렬을 해준다
right_idx = 0                                    # 제일 오른쪽에 위치한 곳을 지정할 변수
right_height = 0
height_max = 0                                   # 가장 큰 높이를 저장할 변수
height_idx = 0                                 # 가장 큰 높이의 인덱스를 저장할 변수
left_idx = storage[0][0]
left_height = storage[0][1]
for x, y in storage:
    storage_list[x] = y                          # 높이 저장
    right_idx = x                                # 가장 오른쪽에 위치한 곳 저장
    right_height = y
    if y > height_max:                           # 가장 큰 높이와 인덱스를 찾음
        height_max = y
        height_idx = x

answer = 0

for i in range(0, height_idx):
    if left_height < storage_list[i + 1]:
        answer += left_height * (storage[i + 1][0] - storage[i][0])
        left_height = storage_list[i + 1]
    else:
        answer += left_height * (storage[i + 1][0] - storage[i][0])

for i in range(right_idx, height_idx, -1):
    if right_height < storage_list[i - 1]:
        answer += right_height * (storage[i][0] - storage[i - 1][0])
        right_height = storage_list[i + 1]
    else:
        answer += left_height * (storage[i][0] - storage[i - 1][0])

print(answer)