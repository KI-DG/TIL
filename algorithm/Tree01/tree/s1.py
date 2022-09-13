import sys
sys.stdin = open("input")


def inorder(n):
    global answer
    if n:
        inorder(ch1[n])
        answer += answer_list[n]
        inorder(ch2[n])


t = 10

for tc in range(1, t + 1):

    v = int(input())    # 정점 개수, 마지막 정점 번호
    answer_list = ['']  # 문자를 저장할 리스트
    ch1 = [0] * (v + 1)  # 자식 1 저장 할 리스트
    ch2 = [0] * (v + 1)  # 자식 2 저장 할 리스트
    answer = ''
    for i in range(v):
        arr = list(input().split())
        idx, alp = int(arr[0]), arr[1]

        if len(arr) == 4:
            ch1[idx], ch2[idx] = int(arr[2]), int(arr[3])
        elif len(arr) == 3:
            ch1[idx] = int(arr[2])
        answer_list.append(alp)

    inorder(1)
    print(f'#{tc} {answer}')