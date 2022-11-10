import sys

sys.stdin = open('input.txt')


def merge(left, right):
    global case

    merged_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    if left[-1] > right[-1]:
        case += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # 더이상 분할할 수 없을때 다시 리턴 (종료조건)

    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    case = 0
    sort_data = merge_sort(data)
    print(f'#{tc} {sort_data[n // 2]} {case}')