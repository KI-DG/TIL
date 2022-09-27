import sys

sys.stdin = open('input.txt')


def search(arr, left, right, value):
    global answer
    center = (left + right) // 2   # left = start ~ center - 1 right = m + 1 ~ end
    if arr[center] == value:
        answer += 1
        return answer
    else:
        search(arr, left, center - 1, value)


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    data1_list = list(map(int, input().split()))
    data2_list = list(map(int, input().split()))

    quick_sort(data2_list, 0, len(data2_list) - 1)
    answer = 0

    for x in data2_list:
        if x in data1_list:
            start, end = 0, m - 1
            search(data2_list, start, end, x)

    print(f'#{tc} {answer}')

    # 런타임 에러 4개만 맞는다 정렬된게 대부분인데 퀵정렬을 돌려서 그런거 같다