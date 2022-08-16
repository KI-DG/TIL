# 새로운 불면증 치료법
import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    n = input()
    value = int(n)
    data = [0]*10   # [0] 0~9가 들어갈 리스트를 만들어준다.
    while True:     # while문으로 숫자가 다나올 때까지 만들어준다.
        for i in range(len(n)):
            data[int(n[i])] += 1
        if not data.count(0):   # 0이 없으면 다 있는 거이기 때문에 조건문을 만들어 준다.
            print(f"#{tc} {int(n)}")
            break   # break를 써서 반복문이 빠져나오게 한다.
        n = str(value + int(n))
        # 0이 존재하면 다 나온게 아니기 때문에 다시 값을 더해줘서 값을 갱신해 준다.
