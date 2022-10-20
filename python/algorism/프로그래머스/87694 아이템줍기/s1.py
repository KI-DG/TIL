def solution(rectangle, characterX, characterY, itemX, itemY):
    n = len(rectangle)
    arr = [[0] * 50 for _ in range(50)]

    # 상자가 있는 곳을 0 으로 표시
    for i in range(n):
        for j in range(rectangle[i][0], rectangle[i][2] + 1):
            for k in range(rectangle[i][1], rectangle[i][3] + 1):
                arr[k][j] += 1

    arr[characterY][characterX] = 99  # 시작 위치
    arr[itemY][itemX] = 100  # 아이템 위치

    answer = 0
    return answer


a = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
b = 1
c = 3
d = 7
e = 8
solution(a, b, c, d, e)

