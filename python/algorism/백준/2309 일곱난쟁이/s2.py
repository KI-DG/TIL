import sys

sys.stdin = open("input.txt")

dwarfs = [int(input()) for _ in range(9)]               # 난쟁이 수가 9 명
sum_height = sum(dwarfs)                                # 난쟁이 키 값

for i in range(8):                                      # 한명은 포함되었으니 8번 반복
    for j in range(i + 1, 9):                           # 그 다음 부터 한명 반복해야 되니까 
        if sum_height - dwarfs[i] - dwarfs[j] == 100:   # 키가 100이면
            a, b = dwarfs[i], dwarfs[j]                 # 그 값을 빼준다
            dwarfs.remove(a)
            dwarfs.remove(b)
            break

    if len(dwarfs) == 7:                                # 반복문을 빨리 탈출하기위해 (가지치기)
        break

dwarfs.sort()                                           # 오름차순 정렬

for i in dwarfs:                                        # 세로로 출력
    print(i)
