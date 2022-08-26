import sys

sys.stdin = open('input')

t = int(input())


def cheksudoku(m):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            # 세로 검사
            row = m[i][j]
            # 가로 검사
            col = m[j][i]
            # 만약에 숫자가 중복이 된다면 0을 리턴
            if row_num[row]:
                return 0
            if col_num[col]:
                return 0

            row_num[row] = 1
            col_num[col] = 1
            # 3X3 의 공간에서 있는지 없는지 확인한다.
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = m[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1


for tc in range(1, t + 1):
    mat = [list(map(int, input().split())) for _ in range(9)]

    result = cheksudoku(mat)

    print(f'#{tc} {result}')





