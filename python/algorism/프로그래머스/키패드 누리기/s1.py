dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(numbers, hand):

    left_hand = [1, 4, 7]
    right_hand = [3, 6, 9]
    key_pad = [[0] * 3 for _ in range(4)]
    result = []
    cnt = 0
    k = 1
    for i in range(4):
        for j in range(3):
            key_pad[i][j] = k
            k += 1

    key_pad[3][2], key_pad[3][0], key_pad[3][1] = '#', '*', 0

    left_start = key_pad[3][0]
    right_start = key_pad[3][2]
    for number in numbers:
        cnt += 1
        if number in left_hand:
            result.append('L')
        elif number in right_hand:
            result.append('R')
        elif number == left_start:
            result.append('L')
        elif number == right_start:
            result.append('R')
        for x in range(4):
            for y in range(3):
                if number == key_pad[x][y]:
                    if number in left_hand:
                        left_start = key_pad[x][y]
                        break
                    elif number in right_hand:
                        right_start = key_pad[x][y]
                        break
                    else:
                        for p in range(1, 4):
                            if cnt == len(result):
                                break
                            for k in range(4):
                                nx = x + dx[k] * p
                                ny = y + dy[k] * p

                                if 0 <= nx < 4 and 0 <= ny < 3:
                                    if hand == 'left':
                                        if key_pad[nx][ny] == left_start:
                                            result.append('L')
                                            left_start = key_pad[x][y]
                                            break
                                        elif key_pad[nx][ny] == right_start:
                                            result.append('R')
                                            right_start = key_pad[x][y]
                                            break
                                    if hand == 'right':
                                        if key_pad[nx][ny] == right_start:
                                            result.append('R')
                                            right_start = key_pad[x][y]
                                            break
                                        elif key_pad[nx][ny] == left_start:
                                            result.append('L')
                                            left_start = key_pad[x][y]
                                            break
    print(''.join(result))


# arr = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
arr1 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = 'right'
b = 'left'
# solution(arr, a)
solution(arr1, b)
# solution(arr2, a)
# LRLLRRLLLRR
