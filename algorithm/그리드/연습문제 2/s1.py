'''
4
124783
667767
054060
101123
'''
'''
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때 3장의
카드가 연속적인 번호를 갖는 경우 run, 3장의 카드가 동일한 번호를 갖는경우르
triplet// run과 triplet으로 구성된 경우 Baby-Gin이라 함
'''


def baby_gin(n):
    global answer
    triplet = 0
    run = 0
    if n == len(arr):
        if arr[0] == arr[1] == arr[2]:
            triplet += 1
        if arr[2] == arr[1] + 1 == arr[0] + 2:
            run += 1
        if arr[3] == arr[4] == arr[5]:
            triplet += 1
        if arr[5] == arr[4] + 1 == arr[3] + 2:
            run += 1
        if run + triplet == 2:
            answer = True
            return answer
    else:
        for i in range(n, len(arr)):
            arr[n], arr[i] = arr[i], arr[n]
            baby_gin(n + 1)
            arr[n], arr[i] = arr[i], arr[n]


t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input()))

    answer = False
    baby_gin(0)
    print(f'#{tc} {answer}')