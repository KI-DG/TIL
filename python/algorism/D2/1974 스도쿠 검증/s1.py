import sys

sys.stdin = open("input.txt")


def sudoku(arr):
    for row in range(9):
        row_num = [0] * 10   
        col_unm = [0] * 10
        for col in range(9):
            vertical = arr[row][col]  # 세로 검사
            width = arr[col][row]   # 가로 검사

            if row_num[vertical]:       # 만약 row_num 에 0이 아니라면
                return 0
            if col_unm[width]:          # 만약 col_num 에 0이 아니라면
                return 0

            row_num[vertical] = 1       # 카운팅으로 1을 채워준다
            col_unm[width] = 1

            if row % 3 == 0 and col % 3 == 0:  # 둘다 3의 배수 이면 사각형 안에도 탐색
                square = [0] * 10
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        num = arr[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1


t = int(input())

for tc in range(1, t + 1):
    data = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    print(f'#{tc} {sudoku(data)}')