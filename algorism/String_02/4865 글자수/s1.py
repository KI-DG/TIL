import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    str1 = list(input())
    str2 = list(input())

    str_list = [0] * len(str1)  # [0] 카운트할 수 있는 리스트를 만들어 준다.

    for idx, val in enumerate(str1):
        for idx2, val2 in enumerate(str2):
            if val == val2:
                str_list[idx] += 1  # 반복문을 통해 글자가 몇개가 나오는지 확인

    str_max = 0
    for i in range(len(str_list)):   # 반복문을 통해 리스트에 최대값을 찾는다.
        if str_max <= str_list[i]:
            str_max = str_list[i]

    print(f'#{tc} {str_max}')