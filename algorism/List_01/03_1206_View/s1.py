import sys

sys.stdin = open("input.txt")

    # 테스트를 가져온다.

for tc in range(1, 11):  # 테스트 케이스를 가져와 반복문으로 풀어준다.
    N = int(input())
    height_list = list(map(int, input().split()))
    height_sum = 0   # 조망권의 합을 담는 변수


    for i in range(2, N-2):
        # 양쪽 두개의 idx는 0이라 빼준다.
        if height_list[i] > height_list[i+1] and height_list[i] > height_list[i+2] and height_list[i] > height_list[i-1] and height_list[i] > height_list[i-2] :
        # 두 칸의 조망권이 발생하였을 경우
            height_sum += (height_list[i] - max(height_list[i-1], height_list[i-2], height_list[i+1], height_list[i+2]))
        # 나머지 네칸에서 제일 높은 값하고 i번째의 값을 빼준다.

    print(f'#{tc} {height_sum}')
