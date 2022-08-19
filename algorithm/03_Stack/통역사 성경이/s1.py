import sys

sys.stdin = open('input')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 문장의 개수
    name = input()
    print(f'#{tc}', end=' ')
    # 문장들
    name = name.replace('!', '.').replace('?', '.')
    # 기준을 하나로 통일 시켜준다.
    name_split = name.split('.', n)
    # 기준을 토대로 문장을 나눠준다.
    for i in range(n):
        x = name_split[i]
        y = x.split()
        count = 0
        for j in range(len(y)):
            if y[j].title():
                count += 1

        print(f'{count}', end=' ')
    print()






