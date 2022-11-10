import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    number = int(input())  # 앞에 0이 있어서 문자열로 받아줘야된다.
    ai = input()
    card = [0]*10  # 테스트 마다 숫자가 다르다.

    ai_list = list(ai)  # 한 글자씩 정렬을 하기 위해 문자열을 리스트로 변환
    int_list = list(map(int, ai_list)) # 문자열을 정수로 변환

    for i in int_list:  # count하기
        card[int(i)] += 1

    largest = card[0]    # 제일 많이 나온 수 찾기
    largest_index = 0   # 제일 많이 나온 수의 index찾기
    for i, j in enumerate(card):
        if j >= largest:
            largest = j
            largest_index = i

    print(f'#{tc} {largest_index} {largest}')
